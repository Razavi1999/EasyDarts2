from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from Account.forms import *


def registration_view(request):
    context = {}
    if request.POST:
        Myform = RegistrationForm(request.POST)
        if  Myform.is_valid():
            Myform.save()
            email = Myform.cleaned_data.get('email')
            raw_password = Myform.cleaned_data.get('password1')

            account = authenticate(email=email,password=raw_password)
            login(request , account)
            return redirect('home')

        else:
            context['registration_form'] = Myform

    else:
        Myform = RegistrationForm()
        context['registration_form'] = Myform

    return render(request, 'account/register.html' ,context)

def logout_view(request):
    login(request)
    return redirect('/')

def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password=password)

            if user:
                login(request,user)
                return redirect('home')

    else:
        form = AccountAuthenticationForm()


    context['login_form'] = form
    return render(request,"account/login.html", context)

def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(

            initial={
                "email": request.user.email,
            }
        )

    context['account_form'] = form

    # blog_posts = BlogPost.objects.filter(author=request.user)
    # context['blog_posts'] = blog_posts

    return render(request, "account/account.html", context)


def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html', {})

