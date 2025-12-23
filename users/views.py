from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "User created successfully")
            return redirect("todolist")
    else:
        register_form = RegistrationForm()

    return render(request, "register.html", {"register_form": register_form})


def login():
    return render("todolist.html")


def logout():
    return render("login.html")