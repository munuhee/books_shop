from django.urls import path
from .views import ebook_list, ebook_detail, add_ebook

urlpatterns = [
    path('', ebook_list, name='ebook_list'),
    path('<int:pk>/', ebook_detail, name='ebook_detail'),
    path('add/', add_ebook, name='add_ebook'),
]
