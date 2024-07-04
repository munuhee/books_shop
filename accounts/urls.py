from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_change/', views.password_change, name='password_change'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path(
        'address_update/<int:address_id>/',
        views.address_update,
        name='address_update'
    ),
    path('profile/', views.profile_view, name='profile_view'),
]
