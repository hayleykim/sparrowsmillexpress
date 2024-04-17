from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('menu/create', views.MenuCreate.as_view(), name='menu_create'),
    path('menu/<int:pk>/update/', views.MenuUpdate.as_view(), name='menu_update'),
    path('menu/<int:pk>/delete/', views.MenuDelete.as_view(), name='menu_delete'),
    path('menu/<int:menu_id>/add_photo/', views.add_photo, name='add_photo'),

    path('accounts/signup/', views.signup, name='signup'),

]