# todolist/views.py
from django.http import HttpResponse
from django.shortcuts import render , redirect
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator


def todolist(request):
    return HttpResponse("<h1> Welcome To This Page </h1>") 

def base(request):
    return render(request , "base.html", {})


def dashboard(request):
    name  = {
        'name' : 'Prasad'
    }
    return render(request, "dashboard.html" , name)

def home(request):
    name = {
        'name' : 'Prasad'
    }
    

    return render(request , "home.html", name)

def delete_task(request,task_id):
    task_obj = Task.objects.get(id=task_id)
    task_obj.delete()
    messages.success(request,f"Task-{task_obj.task} deleted.")
    return redirect("todolist")

def edit_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    if request.method == "POST":
        form_data = TaskForm(request.POST, instance=task_obj)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Task Updated Successfully.")
            return redirect("todolist")   # <-- replace with your actual URL name
    else:
        form_data = TaskForm(instance=task_obj)

    context = {
        "form": form_data,
        "task_obj": task_obj
    }

    return render(request, "edit.html", context)

def complete_task(request,task_id):
    task_obj = Task.objects.get(id=task_id)
    task_obj.is_completed = True
    task_obj.save()
    messages.success(request,"Task Status Updated.")
    return redirect("todolist")

def pending_task(request , task_id):
    task_obj = Task.objects.get(id=task_id)
    task_obj.is_completed = False
    task_obj.save()
    messages.success(request,"Task Status Updated..")
    return redirect("todolist")


def about_us(request):
    name = {
        'name' : 'Prasad'
    }
    return render(request, "aboutus.html", name)

def todolist(request):
    if request.method == "POST":
        form_data = TaskForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Task Added Successfully")
            return redirect("todolist")  # reload page after saving
    else:
        form_data = TaskForm()

    # ✅ Define all_tasks after handling POST/GET
    all_tasks = Task.objects.all()
    paginator = Paginator(all_tasks,5)
    page = request.GET.get("page")
    all_tasks = paginator.get_page(page)



    context = {
        'name': 'Prasad',
        'form_data': form_data,
        'all_tasks': all_tasks,
    }

    return render(request, "todolist.html", context)


