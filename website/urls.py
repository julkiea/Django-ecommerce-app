from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about_us/', views.about_us, name = 'about_us'),
    path('login/', views.login_user, name = 'login_user'),
    path('logout/', views.logout_user, name = 'logout_user'),
    path('register/', views.register_user, name = 'register_user'),
]