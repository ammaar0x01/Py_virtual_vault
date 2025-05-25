"""
controller_task.py 
==================
"""
from flask import render_template, request, redirect, url_for, flash, Blueprint    
from datetime import datetime as dt 

from dependencies._constants import DTO, DEFAULT_USER
# ----------------------------

task_blueprint = Blueprint("controller_task", __name__)
# ----------------------------


# ---GET---
@task_blueprint.route("/tasks")
def tasks_get(): 
    data = DTO.get_all_records("Task")
    return render_template(
        "tasks.html", 
        tasks=data, 
        filter_option="All"    
    )
# -------------------------------------

# ---POST--- 
@task_blueprint.route("/tasks", methods=["POST"])
def tasks_post(): 
    task_text = request.form.get("task-text")
    task_details = request.form.get("task-details") 
    task_details = "No details" if task_details == "" else task_details 

    is_priority = request.form.get("is-priority")
    is_priority = True if is_priority == "yes" else False  

    is_repetititve = request.form.get("is-repetitive")
    is_repetititve = True if is_repetititve == "yes" else False 

    user_id = DEFAULT_USER[0]
    now = dt.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(task_text, task_details, is_priority, user_id)

    if (len(task_text) < 30):
        record = (task_text, task_details, is_priority, is_repetititve, formatted_date, user_id)
        DTO.insert_record_auto("Task", record)
        flash("New task added")
        return redirect(url_for("controller_task.tasks_get"))
    
    flash("Task name is too long. Add more details to the details section")
    print("\n***Invalid Input***")
    return redirect(url_for("controller_task.tasks_get"))

### filter 
@task_blueprint.route("/tasks-filter", methods=["POST"])
def tasks_post_filter():
    task_filter = request.form.get("task-filter")

    if task_filter == "All": 
        return redirect(url_for("controller_task.tasks_get"))

    elif task_filter == "Priority":  
        data = DTO.get_records("Task", "is_priority", True)
        flash("Filter applied")
        return render_template(
            "tasks.html", 
            tasks=data, 
            filter_option="Priority"    
        )

    data = DTO.get_records("Task", "is_repetitive", True)
    flash("Filter applied")
    return render_template(
        "tasks.html", 
        tasks=data, 
        filter_option="Repetitive"    
    )
# -------------------------------------

# ---PUT---  
@task_blueprint.route("/update-task/<int:id>", methods=["POST", "GET"])
def tasks_put(id):
    if request.method == 'POST':
        text = request.form["update-task-text"]
        details = request.form["update-task-details"]
        details = "No details" if details == "" else details 

        is_priority = request.form.get("update-is-priority")
        is_priority = True if is_priority == "yes" else False  

        is_repetititve = request.form.get("update-is-repetitive")
        is_repetititve = True if is_repetititve == "yes" else False 

        print(id, text, details, is_priority)
        cols = ["task_text", "task_details", "is_priority", "is_repetitive"]
        values = [text, details, is_priority, is_repetititve]

        DTO.update("Task", "task_id", id, cols, values)
        flash("Task updated")
        return redirect(url_for('controller_task.tasks_get'))
    
    task = DTO.get_record("Task", "task_id", id)
    return render_template('update-task.html', task=task)
# -------------------------------------

# ---DELETE--- 
@task_blueprint.route("/delete-task/<int:id>", methods=["GET"])
def tasks_delete(id):
    flash("Task deleted")
    DTO.delete("Task", "task_id", id)
    return redirect(url_for('controller_task.tasks_get'))
# ======================================

