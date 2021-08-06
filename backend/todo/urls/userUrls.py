from django.urls import path 
from . import views

urlpatterns = [ 
   path('list/', views.userList, name='user-list'),
    path('detail/<str:pk>/', views.userDetail, name='user-detail'),
    path('create/', views.userCreate, name='user-create'),
    path('update/<str:pk>/', views.userUpdate, name='user-update'),
    path('delete/<str:pk>/', views.userDestroy, name='user-destroy') 
]