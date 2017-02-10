from django.shortcuts import render
from django.contrib.auth import authenticate, login
from genealogy_app.forms import LoginForm, CreateAccountForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.models import User

# Create your views here.
class LoginView(View):

    def get(self,request):

        form = LoginForm()
        return render(request,'login_form.html', {'form': form})

    def post(self,request):

        form = LoginForm(request.POST)        
        u = request.POST['login']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            next=request.GET.get("next")
            if next:
                return redirect(next)
            else:
                return HttpResponse("Logowanie poprawne")
            
        else:
            form.add_error(None, "Wrong login or password")
            return render(request,'login_form.html', {'form': form})

class mainPage(View):
    
    def get(self,request):
        return render (request, 'index.html')

class CreateAccount(View):

    def get(self, request):
        form = CreateAccountForm()
        return render(request, "user_form.html", {"form": form})

    def post(self, request):
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['login']
            pass1 = form.cleaned_data['password']
            pass2 = form.cleaned_data['password2']
            em = form.cleaned_data['email']

            if pass1 == pass2:
                a = User.objects.create_user(username = user, password = pass1, email = em)
                a.save()
        
            else:
                return HttpResponse("<h1>Your password is incorrect.</h1>")

        return redirect("/login")

        