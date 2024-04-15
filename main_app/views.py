from django.shortcuts import render
from .models import Menu

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def menu(request):
    menus = Menu.objects.all()
    return render(request, 'menu.html', {
        'menu': menus
    })

def menu_list(request):
    menus = Menu.objects.all()
    
    menus_by_category = {}
    for menu in menus:
        category = menu.get_category_display()
        if category not in menus_by_category:
            menus_by_category[category] = []
        menus_by_category[category].append(menu)
    
    context = {
        'menus_by_category': menus_by_category
    }
    
    return render(request, 'menu.html', context)


class MenuCreate(CreateView):
    model = Menu
    fields = '__all__'


class MenuUpdate(UpdateView):
    model = Menu
    fields = '__all__'

class MenuDelete(DeleteView):
    model = Menu
    success_url = '/menu/'