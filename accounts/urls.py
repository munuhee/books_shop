from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_change/', views.password_change, name='password_change'),
    path('customer_update/', views.customer_update, name='customer_update'),
    path('customer/', views.customer_view, name='customer_view'),
]
