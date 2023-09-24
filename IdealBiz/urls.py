"""IdealBiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register, name="user-register"),
    path('home/',user_views.home, name="home"),
    path('login/',auth_view.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/',auth_view.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('passwordreset/',auth_view.PasswordResetView.as_view(template_name="users/password_reset.html"), name="password_reset"),
    path('passwordreset/done/',auth_view.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
    path('passwordreset/confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),
    path('passwordreset/complete/',auth_view.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete")
     
]
