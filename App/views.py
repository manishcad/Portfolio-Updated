
from django.shortcuts import render, redirect
from .models import Certificate, Projects, Review
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import logout_then_login
from .forms import Register_Form
from django.core.paginator import Page, PageNotAnInteger, Paginator, EmptyPage
# Create your views here.


def home(request):
    page = request.GET.get('page')
    projects = Projects.objects.all()[::-1]
    certificates = Certificate.objects.all()[::-1]

    paginator = Paginator(projects, 3)
    projects = paginator.get_page(page)

    context = {'projects': projects,
               'certificates': certificates, 'paginator': paginator}
    return render(request, 'index.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        project_type = request.POST.get("project type")
        budget = request.POST.get("budget")
        try:
            details = request.POST.get("details")

            send_mail("JOB POST", f"Client Name: {name}\n,Client Email: {email}\n,Project Type: {project_type}\n,Budget:{budget} \n Message {details} ", "manishtochand@gmail.com",
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


def single_project(request, pk):
    project = Projects.objects.get(id=pk)
    reviews = Review.objects.filter(project=pk)

    if request.method == "POST":
        if request.user.is_authenticated:

            user = request.user
            vote = request.POST.get('vote')
            if vote == "Up Vote":
                project.total_up_vote = project.total_up_vote+1
                project.save()
            else:
                print("Giving Down Vote")
            message = request.POST.get('comment')
            form = Review(project=project, owner=user,
                          vote=vote, body=message)
            form.save()
        else:
            print("Authemtication Error")

    context = {'project': project, 'reviews': reviews}
    return render(request, '7.html', context)


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("Home")
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'Home')
        else:
            messages.warning(request, 'Invalid Credentials')
    return render(request, 'login.html')


def sign_out(request):
    logout_then_login(request, 'Login')
    return redirect('Login')


def register(request):
    if request.user.is_authenticated:
        return redirect("Home")
    form = Register_Form()
    error = ""
    if request.method == "POST":
        form = Register_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect("Login")
        else:
            error = form.errors

    context = {'form': form, 'error': error}
    return render(request, 'register.html', context)


def new_single_project(request, pk):
    return render(request, '7.html')
