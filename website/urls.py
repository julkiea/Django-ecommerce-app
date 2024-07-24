from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about_us/', views.about_us, name = 'about_us'),
    path('login/', views.login_user, name = 'login_user'),
    path('logout/', views.logout_user, name = 'logout_user'),
    path('register/', views.register_user, name = 'register_user'),
    path('product/<int:pk>', views.product, name = 'product'),
    #path('category/<str:foo>', views.category, name = 'category'),
    path('filter_products/', views.filter_products, name = 'filter_products'),
    path('update_user/', views.update_user, name = 'update_user'),
    path('update_password/', views.update_password, name = 'update_password'),
    path('update_info/', views.update_info, name = 'update_info'),
]