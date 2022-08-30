
from django.shortcuts import render, redirect
from .models import Certificate, Projects
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def home(request):

    projects = Projects.objects.all()[::-1]
    certificates = Certificate.objects.all()[::-1]
    print(certificates)
    context = {'projects': projects, 'certificates': certificates}
    return render(request, 'index.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        project_type = request.POST.get("project type")
        budget = request.POST.get("budget")
        try:
            details = request.POST.get("details")

            send_mail("JOB POST", f"Client Name: {name}\n,Client Email: {email}\n,Project Type: {project_type}\n,Budget:{budget}", "manishtochand@gmail.com",
                      ["manishtochand@gmail.com"], fail_silently=False)
            messages.success(
                request, "Thank You For Time.I'll Try To Contact You As Soon As Possible")
            return redirect("Home")
        except Exception as e:
            print(e)
            messages.warning(
                request, "Sorry Some Error Occur Please Try Again")
            return redirect("Contact")
    return render(request, 'contact.html')


def message(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(name, email, message)
        try:
            send_mail("Message From Your Own Website", f"Client Name: {name}\n,Client Email: {email}\n,Client Message: {message}", "manishtochand@gmail.com",
                      ["manishtochand@gmail.com"], fail_silently=False)
            messages.success(
                request, "Thank You For Time.I'll Try To Contact You As Soon As Possible")
            return redirect("Home")
        except Exception as e:
            print(e)
            messages.warning(
                request, "Sorry Some Error Occur Please Try Again")
            return redirect("Messsage")
    return render(request, 'message.html')


def work(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        project_type = request.POST.get("project type")
        interest = request.POST.get("interest")
        try:
            details = request.POST.get("details")

            send_mail("Conversation From Portfolio Website", f"Client Name: {name}\n,Client Email: {email}\n,Project Type: {project_type}\n,Interested In:{interest}\nMessage:{details}", "manishtochand@gmail.com",
                      ["manishtochand@gmail.com"], fail_silently=False)
            messages.success(
                request, "Thank You For Time.I'll Try To Contact You As Soon As Possible")
            return redirect("Home")
        except Exception as e:
            print(e)
            messages.warning(
                request, "Sorry Some Error Occur Please Try Again")
            return redirect("Work")
    return render(request, 'work.html')
