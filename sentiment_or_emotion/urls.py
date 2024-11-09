from django.urls import path
from django.conf.urls import url
from . import views
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view 
from .views import *
from .forms import LoginForm
app_name = 'sentiment_or_emotion'

urlpatterns = [
    url(r'^$', views.choose_sentiment_or_emotion, name="choose_sentiment_or_emotion"),
    path("accounts/signup/", CustomerRegistrationFormView.as_view(), name="signup"),
    path("accounts/login/", auth_view.LoginView.as_view(template_name  = "LoginForm.html" ,
                                                        authentication_form  = LoginForm ), name="login"),
    path("logout/", LogoutView, name="logout"),
    path("accounts/pwdchange/", MyPasswordChangeView.as_view(), name="pwdchange"),
    path("pwdchangedone/",auth_view.PasswordChangeDoneView.as_view(template_name  = "home/home.html" ,), name="pwdchangedone"),
    path("profile/", ProfileFormPageView.as_view(), name="profile"),
    path("contact/", Contact, name="contact"),
    path("about/", About, name="about"),


]