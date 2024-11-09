from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View, TemplateView
from django.shortcuts import render , redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import  logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_view 
from .models  import *
from .forms import *

def choose_sentiment_or_emotion(request):
    return render(request, 'home/home.html')

class CustomerRegistrationFormView(TemplateView):
    def get(self , request):
        form = CustomerRegistrationForm()
        return render(request , "CustomerRegistrationForm.html", {"form" : form} )
    
    def post(self , request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request , " Congratulations :) Registered SucessFully ! Please Login ")
            form.save()
        
        return render(request , "CustomerRegistrationForm.html", {"form" : form} )
    
class ProfileFormPageView(TemplateView):
    def get(self ,request):
        form = ProfileForm()
        return render(request , "ProfilePage.html", {"form" : form} )
    
    def post(self , request):
        user = request.user
        form = ProfileForm(request.POST )
        if form.is_valid():
            print(form.errors)
            profile = form.save(commit=False)
            profile.user = request.user 
            profile.save()
            messages.success(request , " Congratulations :) Profile Added SucessFully !")
        
        return render(request , "ProfilePage.html", {"form" : form} )

class MyPasswordChangeView(auth_view.PasswordChangeView):
    template_name = "PasswordChangeForm.html"
    form_class = MyPasswordChangeForm
    success_url = '/pwdchangedone/'

    def form_valid(self, form):
        user = form.save()
        logout(self.request)  # Call your specific function here
        messages.success(self.request, 'Your password was successfully updated!')
        return super().form_valid(form)
            
def LogoutView(request):
    logout(request)
    messages.success(request , " Sucessfully Loged-Out ! ")
    return redirect('/accounts/login')

def Contact(request):
    return render(request, "Contact.html")
def About(request):
    return render(request, "About.html")