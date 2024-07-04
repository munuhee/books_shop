from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='checkout'),
    path('orders/', views.order_list, name='order_list'),
    path('order/<int:order_id>/', views.order_details, name='order_details'),
]
