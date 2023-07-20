Vue.config.ignoredElements = [/^ion-/]

let app = new Vue({
    el: "#root",
    delimiters: ["[[", "]]"],
    data: {
        newLeads: [], completedLeads: [], tables: [], plans: [], dropedLeads: [], archivedLeads: [], operators: [], filterResult: [],
        detailBlock: {}, canceledBlock: {}, singleLead: {},

        dangerAlert: false, planAlert: false, roleError: false, newLeadError: false, cancelAlert: false, recoverAlert: false, roleUndefined: false, 
        filterBlock: false, loader: true,

        tableId: 0, showBlock: 1, accountId: 0, errorAudio: "error.mp3",

        accountRole: "", tableTitle: "", tablePriority: "", fio: "", phone: "", plan: "", social: "", comment: "", leadComment: "", 
        reminder: "", filterOperator: "0", filterPlan: "0", filterDate: "", searchInput: "", archiveSearchInput: "", dropSearchInput: "",
    },
    mounted() {
        fetch("get_leads/", {method: "POST", headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken}, 
        body: JSON.stringify({"status": 200})}).then(resp => resp.json()).then(data => {
            if (data.status != 404){
                this.accountRole = data.account_role, this.accountId = data.account_id
                this.newLeads = data.new, this.completedLeads = data.completed, this.tables = data.tables, this.plans = data.plans, 
                this.dropedLeads = data.droped, this.archivedLeads = data.archived, this.operators = data.operators
    
                if (+this.accountRole >= 0){
                    if ([3].includes(+this.accountRole)){
                        this.tables.forEach(table => {table.leads = table.leads.filter(item => item.operator_id == +this.accountId)});
                        this.completedLeads = this.completedLeads.filter(item => item.operator_id == +this.accountId)} 
                    else if (+this.accountRole > 3){document.querySelector("body").remove()} 
                    else{/*pass*/}
                } else{this.loader = false; this.roleUndefined = true; let audio = new Audio(`/static/crm/audio/${this.errorAudio}`); audio.play()}
    
                this.loader = false;
    
                setInterval( () => {
                    let time = new Date(); let month = ""; let hour = ""; let day = ""
                    if (time.getMonth() < 10){month = `0${time.getMonth()+1}`}else{month = `${time.getMonth()+1}`}
                    if (time.getHours() < 10){hour = `0${time.getHours()}`}else{hour = `${time.getHours()}`}
                    if (time.getDate() < 10){day = `0${time.getDate()}`}else{day = `${time.getDate()}`}
        
                    let timer = time.getFullYear() + month + day + hour + time.getMinutes()
                    let leads = document.querySelectorAll(".single-lead");
                   
                    this.newLeads.forEach(item => {if (item.reminder) {
                        item.reminder = item.reminder.replace("T", "");item.reminder = item.reminder.replace("-", "");
                        item.reminder = item.reminder.replace("-", "");item.reminder = item.reminder.replace(":", "");
                        if (+timer >= +item.reminder){
                            leads.forEach(lead => {if (lead.dataset.order == item.id){lead.classList.add("danger-border")}})}
                        }else{leads.forEach(lead => {if (lead.dataset.order == item.id){lead.classList.remove("danger-border")}})}
                    });

                    this.tables.forEach(table => {table.leads.forEach(lead => {if (lead.reminder){
                        lead.reminder = lead.reminder.replace("T", "");lead.reminder = lead.reminder.replace("-", "");
                        lead.reminder = lead.reminder.replace("-", "");lead.reminder = lead.reminder.replace(":", "");
                        if (+timer >= +lead.reminder){
                            leads.forEach(item => {if (item.dataset.order == lead.id){item.classList.add("danger-border")}})}
                        }else{leads.forEach(item => {if (item.dataset.order == lead.id){item.classList.remove("danger-border")}})}
                    })})
                
                }, 3000)
    
                setInterval( () => {
                    fetch("completed/leads/count/").then(resp => resp.json()).then(data => {if (data.status == 200) {
                        data.data.forEach(item => {this.archivedLeads.push(item); 
                            this.newLeads = this.newLeads.filter(lead => lead.id != item.id)
                            this.tables.forEach(table => {table.leads = table.leads.filter(lead => lead.id != item.id)})
                            this.completedLeads = this.completedLeads.filter(lead => lead.id != item.id)
                        }) 
                    } else{/*pass*/}})  
                }, 300000)
            } else(this.roleUndefined = true)
        })
    },
    methods: {

        changeBlock(dir){
            this.showBlock = dir
            if (+dir == 1){ 
                let leads = document.querySelectorAll(".single-order"); leads.forEach(item => item.classList.remove("d-none")); this.searchInput = ""} 
            else if (+dir == 4){
                let leads = document.querySelectorAll(".archive-fio"); 
                leads.forEach(item => item.parentElement.classList.remove("d-none")); this.archiveSearchInput = ""}
            else if (+dir == 3){
                let leads = document.querySelectorAll(".drop-fio"); 
                leads.forEach(item => item.parentElement.classList.remove("d-none")); this.dropSearchInput = ""}
        },

        createTable() {
            let priorities = []
            this.tables.forEach(table => {priorities.push(table.priority)});
            if (this.tableTitle && this.tablePriority){if (priorities.includes(+this.tablePriority)){this.dangerAlert = true, this.planAlert = false} else{
                fetch("table/create/", {method: "POST", headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken}, body: JSON.stringify({
                    title: this.tableTitle, priority: this.tablePriority,
                })}).then(resp => resp.json()).then(data => {
                        if (data.status != 404){
                        this.dangerAlert = false, this.tableTitle = "", this.tablePriority = "", this.tables.push(data), $('#exampleModal').modal('hide');}
                        else{/*pass*/}
                    })
                }
            } else(this.planAlert = true, this.dangerAlert = false)
        },

        editTableTitle() {
            if (this.tableTitle){fetch("table/title/edit/", {method: "POST", headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken}, 
            body: JSON.stringify({title: this.tableTitle, id: this.tableId})}).then(resp => resp.json()).then(data => {
                    if (data.status != 404){
                    this.tables.forEach(item => {if (item.id == data.id){item.title = data.title}}); $('#tableTitleEdit').modal('hide');}
                    else{/*pass*/}
                })
            } else{this.planAlert = true; this.dangerAlert = false}
        },

        deleteTable() {
            let table = this.tables.find(item => +item.id == this.tableId);
            if (table.leads.length > 0){this.dangerAlert = true; this.planAlert = false} else{fetch("table/delete/", {method: "POST", 
            headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken}, body: JSON.stringify({id: +this.tableId})}).then(resp => resp.json())
            .then(data => {
                if (data.status != 404){this.tables = this.tables.filter(item => item.id != this.tableId); $('#tableTitleEdit').modal('hide');}
                else{/*pass*/}
            })}
        },        
    
        allowDrop(event) {
            event.preventDefault();
        },

        drag(event) {
            event.dataTransfer.setData("id", event.target.id);
            this.newLeads.forEach(item => {if (+item.id == +event.target.id){this.singleLead = item}})
            this.completedLeads.forEach(item => {if (+item.id == +event.target.id){this.singleLead = item}})
            this.tables.forEach(item => {item.leads.forEach(lead => {if (+lead.id == +event.target.id){this.singleLead = lead}})})
            
            let audio = new Audio(`/static/crm/audio/${this.errorAudio}`);
            if (event.target.parentElement.dataset.id == "new" && +this.accountRole < 3){this.roleError = true; audio.play()}
            else if (event.target.parentElement.dataset.id == "new"){fetch("lead/process/know/", {method: "POST", headers: {
                "Content-Type": "application/json", "X-CSRFToken": csrftoken}, body: JSON.stringify({id: this.singleLead.id})
            }).then(resp => resp.json()).then(data => {if (data.status == 404){this.newLeadError = true; audio.play()} else{/*pass*/}})} else{/*pass*/}
        },
    
        drop(event) {
            let itemId = event.dataTransfer.getData("id"); 
            let item = document.getElementById(itemId)
            
            try{
                if (itemId){
                    let lead = '';
                    if (event.target.classList.contains("orders-block")){
                        lead = event.target.insertBefore(item, event.target.firstChild);
                    } else if (event.target.classList.contains("single-order")) {
                        lead = event.target.parentElement.insertBefore(item, event.target.nextSibling);
                    } else if (event.target.classList.contains("rounded")){
                        lead = event.target.parentElement.parentElement.insertBefore(item, event.target.parentElement.nextSibling);
                    } else if (event.target.classList.contains("single-item")){    
                        lead = event.target.parentElement.parentElement.parentElement.insertBefore(item, event.target.parentElement.parentElement.nextSibling);
                    } else if (event.target.classList.contains( "date")){
                        lead = event.target.parentElement.parentElement.parentElement.parentElement.insertBefore(
                            item, event.target.parentElement.parentElement.parentElement.nextSibling);
                    } else if (event.target.classList.contains("badge")){
                        lead = event.target.parentElement.parentElement.parentElement.parentElement.parentElement.insertBefore(
                            item, event.target.parentElement.parentElement.parentElement.parentElement.nextSibling);
                    } else {/*pass*/}                                                                     
                    if (this.singleLead.table_id != lead.parentElement.dataset.id) {                                            
                        fetch("process_change/",{method: "POST", headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken}, body: JSON.stringify({
                        id: lead.id, table_id: lead.parentElement.dataset.id})}).then(resp => resp.json()).then(data => {
                            if (data.status != 404){
                                if (data["status"] == "new"){
                                    lead.firstChild.firstChild.firstChild.innerText = data.lead.date; lead.firstChild.lastChild.classList.add("d-none");
                                    this.newLeads.forEach(lead => {if (+lead.id == +data.lead.id){lead.table_id = data.lead.table_id}})
                                    this.completedLeads.forEach(lead => {if (+lead.id == +data.lead.id){lead.table_id = data.lead.table_id}})
                                    this.tables.forEach(item => {item.leads.forEach(lead => {if (+lead.id == +data.lead.id){lead.table_id = data.lead.table_id}})})
                                } else if (data["status"] == "completed"){
                                    lead.firstChild.firstChild.firstChild.innerText = data.lead.date; lead.firstChild.lastChild.classList.remove("d-none");
                                    lead.firstChild.lastChild.lastChild.innerText = data.lead.operator   
                                    lead.firstChild.classList.remove("danger-border")
                                    this.newLeads.forEach(lead => {if (+lead.id == +data.lead.id){lead.table_id = data.lead.table_id; lead.reminder = ""}})
                                    this.completedLeads.forEach(lead => {if (+lead.id == +data.lead.id){lead.table_id = data.lead.table_id; lead.reminder = ""}})
                                    this.tables.forEach(item => {item.leads.forEach(lead => {if (+lead.id == +data.lead.id)
                                        {lead.table_id = data.lead.table_id; lead.reminder = ""}})});
                                } else {
                                    lead.firstChild.firstChild.firstChild.innerText = data.lead.date;
                                    lead.firstChild.lastChild.classList.remove("d-none");
                                    lead.firstChild.lastChild.lastChild.innerText = data.lead.operator   
                                    this.newLeads.forEach(lead => {if (+lead.id == +data.lead.id){lead.table_id = data.lead.table_id}})
                                    this.completedLeads.forEach(lead => {if (+lead.id == +data.lead.id){lead.table_id = data.lead.table_id}})
                                    this.tables.forEach(item => {item.leads.forEach(lead => {if (+lead.id == +data.lead.id){lead.table_id = data.lead.table_id}})})
                                }
                            }else {/*pass*/}
                        })
                    } else {/*pass*/}
                } else {/*pass*/}
            } catch{/*pass*/}
        },

        createLead() {
            if (this.fio != "" && this.phone != "" && this.social != "" && this.plans.includes(this.plan)){
                fetch("lead/create/", {method: "POST", headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken}, body: JSON.stringify({
                    fio: this.fio, phone: this.phone, plan: this.plan, social: this.social, comment: this.comment   
                })}).then(resp => resp.json()).then(data => {
                    if (data.status != 404){this.newLeads.unshift(data); $('#leadCreate').modal('hide');}
                })
            } else if (this.fio != "" && this.phone != "" && this.social != ""){this.planAlert = true; this.dangerAlert = false;}
            else {this.dangerAlert = true; this.planAlert = false}
        },

        leadDetail(id) {
            this.leadComment = ""; this.reminder = ""; this.loader = true
            fetch("lead/detail/", {method: "POST", headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken}, body: JSON.stringify({id: id})})
            .then(resp => resp.json()).then(data => {if (data.status != 404){
                this.detailBlock = data; this.showBlock = 2; if (data.reminder){this.reminder = data.reminder}; this.loader = false
            }})
        },

        commentCreate(id){
            if (this.leadComment){ fetch("lead/comment/create/", {method: "POST", headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken}, 
                body: JSON.stringify({lead_id: id, comment: this.leadComment})}).then(resp => resp.json()).then(data => {
                    if (data.status != 404){this.detailBlock.comments.push(data); this.leadComment = ""}    
                })
            }
        },

        commentPinOrUnpin(id){
            fetch("lead/comment/pin_or_unpin/", {method: "POST", headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken}, 
                body: JSON.stringify({id: id})}).then(resp => resp.json()).then(data => {
                    if (data.status != 404){
                        if (data.status == "pin"){ 
                            let comment = this.detailBlock.comments.find(item => item.id == id);
                            this.detailBlock.comments = this.detailBlock.comments.filter(item => item.id != id);
                            this.detailBlock.comments.unshift(comment);
                            this.detailBlock.comments.forEach(item => {if (item.id == id){item.pin = true}});
                        } else{
                            let comment = this.detailBlock.comments.find(item => item.id == id);
                            this.detailBlock.comments = this.detailBlock.comments.filter(item => item.id != id);
                            this.detailBlock.comments.push(comment);
                            this.detailBlock.comments.forEach(item => {if (item.id == id){item.pin = false}});
                        }
                    }
                }
            )
        },

        reminderCreateOrRemove(id){
            if (this.reminder){
                fetch("reminder/create_or_remove/", {method: "POST", headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken}, 
                body: JSON.stringify({id: id, reminder: this.reminder})}).then(resp => resp.json()).then(data => {
                    if (data.status != 404){
                        if (data.status == "create"){
                            this.detailBlock.reminder = this.reminder;
                            this.newLeads.forEach(item => {if (item.id == id){item.reminder = this.reminder}})
                            this.tables.forEach(item => {item.leads.forEach(lead => {if (lead.id == id){lead.reminder = this.reminder}})})
                        } else{
                            this.detailBlock.reminder = ""; this.reminder = ""; 
                            this.newLeads.forEach(item => {if (item.id == id){item.reminder = ""}})
                            this.tables.forEach(item => {item.leads.forEach(lead => {if (lead.id == id){lead.reminder = ""}})})
                        }
                    }
                })
            }
        },

        canceledDetail(id) {
            this.loader = true;
            fetch("canceled/lead/detail/", {method: "POST", headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken},
            body: JSON.stringify({id: id})}).then(resp => resp.json()).then(data => {
                if (data.status != 404){this.canceledBlock = data; this.loader = false}
            })
        },

        leadRecover(id) {
            fetch("lead/recover/", {method: "POST", headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken},
            body: JSON.stringify({id: id})}).then(resp => resp.json()).then(data => {
                if (data.status != 404){
                    this.dropedLeads = this.dropedLeads.filter(item => item.id != id); this.newLeads.unshift(data);
                    $('#canceledModal').modal('hide'); this.recoverAlert = false
                }
            }) 
        },

        leadCancel(id) {
            fetch("lead/cancel/", {method: "POST", headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken},
            body: JSON.stringify({id: id})}).then(resp => resp.json()).then(data => {
                if (data.status != 404){
                    this.dropedLeads.push(data.data);
                    if (data.old == "new"){this.newLeads = this.newLeads.filter(item => item.id != id)}
                    else if (data.old == "completed"){this.completedLeads = this.completedLeads.filter(item => item.id != id)}
                    else{this.tables.forEach(table => {table.leads = table.leads.filter(item => item.id != id)})}
                    this.cancelAlert = false;
                }
            }) 
        },

        filter() {
            fetch("filter/", {method: "POST", headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken}, body: JSON.stringify({
                operator: this.filterOperator.toString(), plan: this.filterPlan.toString(), date: this.filterDate
            })}).then(resp => resp.json()).then(data => {
                if (data.status != 404){
                    let leads = document.querySelectorAll(".single-order");
                    leads.forEach(item => {if (data.includes(+item.dataset.id)){item.classList.remove("d-none")}else{item.classList.add("d-none")}})
                    this.filterBlock = false; this.filterResult = data; this.searchInput = "";
                }
            })
        },

        search() {
            let fios = document.querySelectorAll(".lead-fio"); let phones = document.querySelectorAll(".lead-phone");
            let inputValue = this.searchInput.toLowerCase();

            fios.forEach((item, i) => {
                if (this.filterResult.length){
                    if (this.filterResult.includes(+item.parentElement.parentElement.dataset.id)){
                        if (item.innerText.toLowerCase().includes(inputValue) || phones[i].innerText.includes(inputValue)){
                            item.parentElement.parentElement.classList.remove("d-none")
                        } else{item.parentElement.parentElement.classList.add("d-none")}
                    } else{/*pass*/}
                } else{
                    if (item.innerText.toLowerCase().includes(inputValue) || phones[i].innerText.includes(inputValue)){
                        item.parentElement.parentElement.classList.remove("d-none")
                    } else{item.parentElement.parentElement.classList.add("d-none")}
                }
            })
        },

        archiveSearch() {
            let fios = document.querySelectorAll(".archive-fio"); let phones = document.querySelectorAll(".archive-phone");
            let plans = document.querySelectorAll(".archive-plan"); let operators = document.querySelectorAll(".archive-operator");
            let socials = document.querySelectorAll(".archive-social"); let dates = document.querySelectorAll(".archive-date");
            let inputValue = this.archiveSearchInput.toLowerCase()

            fios.forEach((item, i) => {
                if (item.innerText.toLowerCase().includes(inputValue) || phones[i].innerText.includes(inputValue) || 
                plans[i].innerText.toLowerCase().includes(inputValue) || dates[i].innerText.includes(inputValue) ||
                operators[i].innerText.toLowerCase().includes(inputValue) || socials[i].innerText.toLowerCase().includes(inputValue)) {
                    item.parentElement.classList.remove("d-none");
                } else{item.parentElement.classList.add("d-none");}
            })
        },

        dropSearch() {
            let fios = document.querySelectorAll(".drop-fio"); let tables = document.querySelectorAll(".drop-table");
            let plans = document.querySelectorAll(".drop-plan"); let socials = document.querySelectorAll(".drop-social"); 
            let dates = document.querySelectorAll(".drop-date"); let inputValue = this.dropSearchInput.toLowerCase();

            fios.forEach((item, i) => {
                if (item.innerText.toLowerCase().includes(inputValue) || tables[i].innerText.toLowerCase().includes(inputValue) || 
                plans[i].innerText.toLowerCase().includes(inputValue) || dates[i].innerText.includes(inputValue) || 
                socials[i].innerText.toLowerCase().includes(inputValue)) {
                    item.parentElement.classList.remove("d-none");
                } else{item.parentElement.classList.add("d-none");}
            })
        },

        commentDelete(id) {
            fetch("comment/delete/", {method: "POST", headers: {"Content-Type": "application/json", "X-CSRFToken": csrftoken}, body: JSON.stringify({
                id: id})}).then(resp => resp.json()).then(data => {
                    if (data.status == 200){this.detailBlock.comments = this.detailBlock.comments.filter(item => item.id != id)}
                    else {/*pass*/}
                })
        },

        cancelAlertBlock() {
            this.cancelAlert = true; let audio = new Audio(`/static/crm/audio/${this.errorAudio}`); audio.play();
        },

        recoverAlertBlock() {
            this.recoverAlert = true; let audio = new Audio(`/static/crm/audio/${this.errorAudio}`); audio.play();
        },

        tablePriorityEdit(id, event) {
            let value = +event.target.value;
            if (value != "" && value >= 0) {
                let table = this.tables.find(item => item.id == id); let tables = this.tables.filter(item => item.id != id);
                let priorities = tables.map(item => item.priority);
                
                if (priorities.includes(value)){this.dangerAlert = true; this.planAlert = false}
                else{this.dangerAlert = false; this.planAlert = false; table.priority = value}
                
            } else{this.dangerAlert = false; this.planAlert = true}
        }
    }
})