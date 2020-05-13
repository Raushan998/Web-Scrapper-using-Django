from django.contrib import admin
from django.urls import path,include
from food import views

app_name='food'
urlpatterns=[
     path('',views.IndexClassView.as_view(),name='index'),
     path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
     path('add/',views.CreateItem.as_view(),name='create_item'),
     path('update/<int:item_id>/',views.update_item,name='update_item'),
     path('remove/<int:item_id>/',views.remove_item,name='remove_item'),
]
