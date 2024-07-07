from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path(
        'product/<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),
]
