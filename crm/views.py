from django.shortcuts import render
from control.models import *
from django.http import JsonResponse
import json
import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser
from crm.models import Lead, Table, LeadComment


def crm_index(request):
    return render(request, "crm/index.html", {"roles": [0,1,2]})


def crm_get_leads(request):
    if request.method == "POST":
        if request.user.account.role: roleCode = request.user.account.role.code
        else: return JsonResponse({"status": 404}, safe=False)

        data = {"new": [], "completed": [], "tables": [], "plans": [], "droped": [], "archived": [], "operators": [],
        "account_role": roleCode, "account_id": request.user.account.id}

        for i in Lead.objects.filter(new=True, complete=False, drop=False, archive=False):
            day = parser.parse(str(i.date_created.strftime("%Y-%m-%d %H:%M")))
            data["new"].append({"fio": i.fio, "social": i.social, "phone": i.phone, "plan": i.plan.title_uz, "reminder": i.reminder, "id": i.id,
                "date": (day + relativedelta(hours=+5)).strftime("%Y-%m-%d %H:%M"), "table_id": "new"
            })
        for i in Lead.objects.filter(complete=True, drop=False, archive=False, new=False):
            day = parser.parse(str(i.date_updated.strftime("%Y-%m-%d %H:%M")))
            data["completed"].append({"fio": i.fio, "social": i.social, "phone": i.phone, "plan": i.plan.title_uz, "id": i.id, "table_id": "completed",
                "operator": f"{i.operator.user.first_name} {i.operator.user.last_name}", "operator_id": i.operator.id,
                "date": (day + relativedelta(hours=+5)).strftime("%Y-%m-%d %H:%M"),
            })
        for i in Lead.objects.filter(drop=True, complete=False, archive=False, new=False):
            day = parser.parse(str(i.date_updated.strftime("%Y-%m-%d %H:%M")))
            data["droped"].append({"fio": i.fio, "social": i.social, "plan": i.plan.title_uz, "id": i.id,
                "droped_table": i.droped_table, "date": (day + relativedelta(hours=+5)).strftime("%Y-%m-%d %H:%M"),
            })
        for i in Lead.objects.filter(archive=True, drop=False, complete=False, new=False):
            day = parser.parse(str(i.date_updated.strftime("%Y-%m-%d")))
            data["archived"].append({"fio": i.fio, "social": i.social, "plan": i.plan.title_uz, "id": i.id, "phone": i.phone, 
                "operator": f"{i.operator.user.first_name} {i.operator.user.last_name}",
                "date": (day + relativedelta(hours=+5)).strftime("%Y-%m-%d"),
            })
        for table in Table.objects.all():
            single_table = {"title": table.title, "priority": table.priority, "id": table.id, "leads": []}
            leads = Lead.objects.filter(table_id=table.id, drop=False, archive=False, complete=False, new=False)
            for i in leads:
                day = parser.parse(str(i.date_updated.strftime("%Y-%m-%d %H:%M")))
                lead = {"fio": i.fio, "social": i.social, "phone": i.phone, "plan": i.plan.title_uz, "id": i.id, "reminder": i.reminder, "table_id": i.table.id,
                "operator": f"{i.operator.user.first_name} {i.operator.user.last_name}", "operator_id": i.operator.id,
                "date": (day + relativedelta(hours=+5)).strftime("%Y-%m-%d %H:%M"),}
                single_table["leads"].append(lead)
            data["tables"].append(single_table)

        for i in Course.objects.all(): data["plans"].append(i.title_uz)

        for i in Account.objects.all(): 
            if i.role: 
                if i.role.code == 3: data["operators"].append({"fio": f"{i.user.first_name} {i.user.last_name}", "id": i.id}) 

        return JsonResponse(data, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)


def crm_table_create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        table = Table.objects.create(title = data["title"], priority = int(data["priority"]))
        obj = {"title": table.title, "priority": table.priority, "id": table.id, "leads": []}
        return JsonResponse(obj, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)


def crm_table_title_edit(request):
    if request.method == "POST":
        data = json.loads(request.body)
        table = Table.objects.get(id = data["id"])
        table.title = data["title"]; table.save()
        obj = {"title": table.title, "id": table.id}
        return JsonResponse(obj, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)


def crm_table_delete(request):
    if request.method == "POST":
        data = json.loads(request.body)
        table = Table.objects.get(id = data["id"])
        table.delete()
        return JsonResponse({"status": 200}, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)


def crm_process_change(request):
    if request.method == "POST":
        data = json.loads(request.body) 
        lead = Lead.objects.get(id=data["id"])
        lead.date_updated = datetime.datetime.now(); lead.save()
        day = parser.parse(str(lead.date_updated.strftime("%Y-%m-%d %H:%M")))
        ready_date = (day + relativedelta(hours=+5)).strftime("%Y-%m-%d %H:%M")
        if data["table_id"] == "new":
            lead.table = None; lead.operator = None; lead.new = True; lead.complete = False; lead.date_created = datetime.datetime.now(); lead.save()
            new_date = parser.parse(str(lead.date_created.strftime("%Y-%m-%d %H:%M")))
            ready_lead = {"id":  lead.id, "date": (new_date + relativedelta(hours=+5)).strftime("%Y-%m-%d %H:%M"), "table_id": "new"}
            return JsonResponse({"lead": ready_lead, "status": "new"}, safe=False)
        elif data["table_id"] == "completed":
            if request.user.account.role.code in [3]: lead.operator = request.user.account
            else: pass
            lead.table = None; lead.new = False; lead.complete = True; lead.reminder = ""; lead.save()
            ready_lead = {"id": lead.id, "date": ready_date, "operator": f"{lead.operator.user.first_name} {lead.operator.user.last_name}", 
            "table_id": "completed", "operator_id": lead.operator.id}
            return JsonResponse({"lead": ready_lead, "status": "completed"}, safe=False)
        else:
            if request.user.account.role.code in [3]: lead.operator = request.user.account
            else: pass
            lead.table_id = int(data["table_id"]); lead.drop=False; lead.archive=False; lead.complete=False; lead.new=False; lead.save()
            ready_lead = {"id": lead.id, "operator": f"{lead.operator.user.first_name} {lead.operator.user.last_name}", "date": ready_date, 
            "table_id": lead.table_id, "operator_id": lead.operator.id}
            return JsonResponse({"lead": ready_lead, "status": 200}, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)


def crm_lead_create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        plan = Course.objects.get(title_uz = data["plan"])
        lead = Lead.objects.create(fio = data["fio"], phone = data["phone"], social = data["social"], plan = plan)
        if data["comment"]:
            LeadComment.objects.create(lead = lead, account = request.user.account, text = data["comment"])
        else: pass
        day = parser.parse(str(lead.date_created.strftime("%Y-%m-%d %H:%M")))
        obj = {"fio": lead.fio, "social": lead.social, "phone": lead.phone, "plan": lead.plan.title_uz, "reminder": lead.reminder, "id": lead.id,
            "date": (day + relativedelta(hours=+5)).strftime("%Y-%m-%d %H:%M"), "table_id": "new"}
        return JsonResponse(obj, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)


def crm_lead_detail(request):
    if request.method == "POST":
        data = json.loads(request.body)
        lead = Lead.objects.get(id=data["id"])

        if lead.operator: operator = f"{lead.operator.user.first_name} {lead.operator.user.last_name}"
        else: operator = ""

        if lead.new: day = parser.parse(str(lead.date_created.strftime("%Y-%m-%d %H:%M"))); table = "Yangi leadlar"
        elif lead.complete: day = parser.parse(str(lead.date_updated.strftime("%Y-%m-%d %H:%M"))); table = "Bajarilib bo`lgan"
        else: day = parser.parse(str(lead.date_updated.strftime("%Y-%m-%d %H:%M"))); table = lead.table.title

        obj = {"fio": lead.fio, "phone": lead.phone, "plan": lead.plan.title_uz, "operator": operator, "customer_comment": lead.customer_comment, "id": lead.id, 
        "social": lead.social, "reminder": lead.reminder, "date": (day + relativedelta(hours=+5)).strftime("%Y-%m-%d %H:%M"), "table": table, "comments": [], 
        "complete": lead.complete}

        for i in lead.leadcomment_set.all():
            day = parser.parse(str(i.date_created.strftime("%Y-%m-%d %H:%M")))
            obj["comments"].append({"account": f"{i.account.user.first_name} {i.account.user.last_name}", "text": i.text, "id": i.id,
                "date": (day + relativedelta(hours=+5)).strftime("%Y-%m-%d %H:%M"), "pin": i.pin, "account_id": i.account.id})
        return JsonResponse(obj, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)


def crm_lead_comment_create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        lead = Lead.objects.get(id=data["lead_id"])
        comment = LeadComment.objects.create(lead = lead, account = request.user.account, text = data["comment"])
        day = parser.parse(str(comment.date_created.strftime("%Y-%m-%d %H:%M")))
        obj = {"account": f"{comment.account.user.first_name} {comment.account.user.last_name}", "text": comment.text, "id": comment.id,
            "date": (day + relativedelta(hours=+5)).strftime("%Y-%m-%d %H:%M"), "pin": comment.pin, "account_id": comment.account.id}
        return JsonResponse(obj, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)


def crm_lead_comment_pin_or_unpin(request):
    if request.method == "POST":
        data = json.loads(request.body)
        comment = LeadComment.objects.get(id=data["id"])
        if (comment.pin): comment.pin = False; comment.save(); return JsonResponse({"status": "unpin"}, safe=False)
        else: comment.pin = True; comment.save(); return JsonResponse({"status": "pin"}, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)
        

def crm_reminder_create_or_remove(request):
    if request.method == "POST":
        data = json.loads(request.body)
        lead = Lead.objects.get(id=data["id"])
        if lead.reminder: lead.reminder = ""; lead.save(); return JsonResponse({"status": "remove"}, safe=False)
        else: lead.reminder = data["reminder"]; lead.save(); return JsonResponse({"status": "create"}, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)


def crm_lead_process_know(request):
    if request.method == "POST":
        data = json.loads(request.body)
        lead = Lead.objects.get(id=data["id"]) 
        if lead.new: return JsonResponse({"status": 200}, safe=False)
        else: return JsonResponse({"status": 404}, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)


def crm_canceled_lead_detail(request):
    if request.method == "POST":
        data = json.loads(request.body)
        lead = Lead.objects.get(id=data["id"], drop=True) 
        if lead.operator: operator = f"{lead.operator.user.first_name} {lead.operator.user.last_name}"
        else: operator = ""
        day = parser.parse(str(lead.date_updated.strftime("%Y-%m-%d %H:%M")))
        obj = {"fio": lead.fio, "phone": lead.phone, "operator": operator, "customer_comment": lead.customer_comment,
        "social": lead.social, "droped_table": lead.droped_table, "plan": lead.plan.title_uz, "id": lead.id,
        "date": (day + relativedelta(hours=+5)).strftime("%Y-%m-%d %H:%M"), "comments": []}

        if lead.leadcomment_set.all():
            for i in lead.leadcomment_set.all():
                day = parser.parse(str(i.date_created.strftime("%Y-%m-%d %H:%M")))
                obj["comments"].append({"account": f"{i.account.user.first_name} {i.account.user.last_name}", "text": i.text, 
                "date": (day + relativedelta(hours=+5)).strftime("%Y-%m-%d %H:%M"), "pin": i.pin})
        else: obj["comments"] = None
        return JsonResponse(obj, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)


def crm_lead_recover(request):
    if request.method == "POST":
        data = json.loads(request.body)
        lead = Lead.objects.get(id=data["id"], drop=True)
        lead.drop = False; lead.new = True; lead.operator = None; lead.date_created = datetime.datetime.now(); lead.date_updated = datetime.datetime.now(); lead.save()
        day = parser.parse(str(lead.date_created.strftime("%Y-%m-%d %H:%M")))
        obj = {"fio": lead.fio, "social": lead.social, "phone": lead.phone, "plan": lead.plan.title_uz, "reminder": lead.reminder, 
        "id": lead.id, "date": (day + relativedelta(hours=+5)).strftime("%Y-%m-%d %H:%M"), "table_id": "new"}
        return JsonResponse(obj, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)


def crm_lead_cancel(request):
    if request.method == "POST":
        data = json.loads(request.body)
        lead = Lead.objects.get(id=data["id"])
        if lead.new: old_process = "new"; lead.droped_table = "Yangi buyurtmalar"; lead.new = False
        elif lead.complete: old_process = "completed"; lead.droped_table = "Bajarilib bo'lganlar"; lead.complete = False
        else: old_process = "table"; lead.droped_table = lead.table.title; lead.table = None
        lead.drop = True; lead.reminder = ""; lead.date_updated = datetime.datetime.now(); lead.save()

        day = parser.parse(str(lead.date_updated.strftime("%Y-%m-%d %H:%M")))
        obj = {"fio": lead.fio, "social": lead.social, "plan": lead.plan.title_uz, "id": lead.id,
            "droped_table": lead.droped_table, "date": (day + relativedelta(hours=+5)).strftime("%Y-%m-%d %H:%M"),}
        return JsonResponse({"data": obj, "old": old_process}, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)
                               
                               
def crm_completed_leads_count(request):
    leads = Lead.objects.filter(complete=True, archive=False, drop=False, new=False)
    data = []
    if len(leads) >= 100:
        for i in leads: 
            i.complete = False; i.archive = True; i.table = None; i.date_updated = datetime.datetime.now(); i.save()
            day = parser.parse(str(i.date_updated.strftime("%Y-%m-%d")))
            data.append({"fio": i.fio, "social": i.social, "plan": i.plan.title_uz, "id": i.id, "phone": i.phone, 
                "operator": f"{i.operator.user.first_name} {i.operator.user.last_name}",
                "date": (day + relativedelta(hours=+5)).strftime("%Y-%m-%d")})
        return JsonResponse({"status": 200, "data": data}, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)


def crm_filter_leads(request):
    if request.method == "POST":
        data = json.loads(request.body)
        arr= []

        if data["operator"] != "0" and data["plan"] != "0" and data["date"]:
            plan = Course.objects.get(title_uz = data["plan"])
            leads = Lead.objects.filter(
                operator_id = data["operator"], plan = plan, date_updated__contains = data["date"], drop = False, archive = False)
            for i in leads: arr.append(i.id)

        elif data["operator"] != "0" and data["plan"] != "0":
            plan = Course.objects.get(title_uz = data["plan"])
            leads = Lead.objects.filter(operator_id = data["operator"], plan = plan, drop = False, archive = False)
            for i in leads: arr.append(i.id)

        elif data["operator"] != "0" and data["date"]:
            leads = Lead.objects.filter(operator_id = data["operator"], date_updated__contains = data["date"], drop = False, archive = False)
            for i in leads: arr.append(i.id)

        elif data["operator"] != "0":
            leads = Lead.objects.filter(operator_id = data["operator"], drop = False, archive = False)
            for i in leads: arr.append(i.id)

        elif data["plan"] != "0" and data["date"]:
            plan = Course.objects.get(title_uz = data["plan"])
            leads = Lead.objects.filter(date_updated__contains = data["date"], plan = plan, drop = False, archive = False)
            for i in leads: arr.append(i.id)

        elif data["plan"] != "0":
            plan = Course.objects.get(title_uz = data["plan"])
            leads = Lead.objects.filter(plan = plan, drop = False, archive = False)
            for i in leads: arr.append(i.id)

        elif data["date"]:
            leads = Lead.objects.filter(date_updated__contains = data["date"], drop = False, archive = False)
            for i in leads: arr.append(i.id)

        else:
            leads = Lead.objects.filter(drop = False, archive = False)
            for i in leads: arr.append(i.id)

        return JsonResponse(arr, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)


def crm_comment_delete(request):
    if request.method == "POST":
        data = json.loads(request.body)
        comment = LeadComment.objects.get(id = data["id"])
        comment.delete()
        return JsonResponse({"status": 200}, safe=False)
    else: return JsonResponse({"status": 404}, safe=False)
