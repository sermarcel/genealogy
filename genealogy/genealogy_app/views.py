from django.shortcuts import render
from django.contrib.auth import authenticate, login
from genealogy_app.forms import LoginForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

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
