from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/create', views.MenuCreate.as_view(), name='menu_create'),
    path('menu/<int:pk>/update/', views.MenuUpdate.as_view(), name='menu_update'),
    path('menu/<int:pk>/delete/', views.MenuDelete.as_view(), name='menu_delete'),

]