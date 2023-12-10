from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('listpage/', views.listpage, name='listpage'),
    path('listpage/<int:pk>', views.editContact, name='editContact'),
    path('listpage/addContact', views.addContact, name='addContact'),
    path('listpage/delete_contact/<str:email>/', views.delete_contact, name='deleteContact'),
    path('listpage/update/<int:pk>', views.update, name='update'),
]
