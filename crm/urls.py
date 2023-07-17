from django.urls import path
from . import views

urlpatterns = [
    path("", views.crm_index, name="crm_index"),
    path("get_leads/", views.crm_get_leads, name="crm_get_leads"),
    path("table/create/", views.crm_table_create, name="crm_table_create"),
    path("table/title/edit/", views.crm_table_title_edit, name="crm_table_title_edit"),
    path("table/delete/", views.crm_table_delete, name="crm_table_delete"),
    path("process_change/", views.crm_process_change, name="crm_process_change"),
    path("lead/create/", views.crm_lead_create, name="crm_lead_create"),
    path("lead/detail/", views.crm_lead_detail, name="crm_lead_detail"),
    path("lead/comment/create/", views.crm_lead_comment_create, name="crm_lead_comment_create"),
    path("lead/comment/pin_or_unpin/", views.crm_lead_comment_pin_or_unpin, name="crm_lead_comment_pin_or_unpin"),
    path("reminder/create_or_remove/", views.crm_reminder_create_or_remove, name="crm_reminder_create_or_remove"),
    path("lead/process/know/", views.crm_lead_process_know, name="crm_lead_process_know"),
    path("canceled/lead/detail/", views.crm_canceled_lead_detail, name="crm_canceled_lead_detail"),
    path("lead/recover/", views.crm_lead_recover, name="crm_lead_recover"),
    path("lead/cancel/", views.crm_lead_cancel, name="crm_lead_cancel"),
    path("completed/leads/count/", views.crm_completed_leads_count, name="crm_completed_leads_count"),
    path("filter/", views.crm_filter_leads, name="crm_filter_leads"),
    path("comment/delete/", views.crm_comment_delete, name="crm_comment_delete"),
]