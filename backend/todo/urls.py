from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [ 
    path('', views.apiOverview, name='api-overview'), 
]

userURLpatterns = [
    path('user/list/', views.userList, name='user-list'),
    path('user/detail/<str:pk>/', views.userDetail, name='user-detail'),
    path('user/create/', views.userCreate, name='user-create'),
    path('user/update/<str:pk>/', views.userUpdate, name='user-update'),
    path('user/delete/<str:pk>/', views.userDestroy, name='user-destroy') ,

    #----------------------------#
    path('todo_list/', views.TODO_LIST.as_view()),
    path('todo_detail/<int:pk>', views.TODO_DETAIL.as_view()),


]

itemURLpatterns = [ 
    path('item/list/<str:auth>/', views.itemList, name='item-list'),
    path('item/list/<str:auth>/<str:accessed>/', views.itemList, name='item-list-accessed'),
    path('item/detail/<str:auth>/<str:itemId>/', views.itemDetail, name='item-detail'),

    # Duc edited here
    path('item/create/', views.ITEM_CREATE.as_view(), name='item-create'),
    path('item/create/<str:auth>/', views.ITEM_CREATE.as_view(), name='item-create'),
    #--------------#

    path('item/update/<str:pk>/', views.ITEM_UPDATE.as_view(), name='user-update'),  #Duc edited here
    path('item/delete/<str:pk>/', views.userDestroy, name='user-destroy') 
]


urlpatterns.extend(userURLpatterns)
urlpatterns.extend(itemURLpatterns)
urlpatterns = format_suffix_patterns(urlpatterns)