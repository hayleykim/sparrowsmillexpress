from django.http import HttpResponseRedirect
import uuid
import boto3
import os
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from .models import Menu, Photo
from .forms import ContactForm, MenuForm, PhotoUploadForm

def home(request):
    return render(request, 'home.html')


def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('contact/emails/contactform.html', {
                'name': name,
                'email': email,
                'content': content
            })

            send_mail('SME Enquiry', 'Message', email, ['barleyhillsinfo@gmail.com'], html_message=html)

            return redirect('about')
    else:
        form = ContactForm()

    return render(request, 'about.html', {
        'form': form
    })


def menu(request):
    menus = Menu.objects.all()
    
    #sorting m in menus based on Menu.CATEGORY_ORDER dictionary & id
    sorted_menus = sorted(menus, key=lambda m: (Menu.CATEGORY_ORDER.get(m.category, 99), m.id))
    
    menus_by_category = {}
    for menu in sorted_menus:
        category = menu.get_category_display()
        if category not in menus_by_category:
            menus_by_category[category] = []
        menus_by_category[category].append(menu)
    
    context = {
        'menus_by_category': menus_by_category
    }
    
    return render(request, 'menu.html', context)


class MenuCreate(LoginRequiredMixin, CreateView):
    model = Menu
    form_class = MenuForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)

        menu_id = self.object.id
        photo_file = self.request.FILES.get('photo-file', None)

        if photo_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            try:
                bucket = os.environ['S3_BUCKET']
                s3.upload_fileobj(photo_file, bucket, key)
                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                Photo.objects.create(url=url, menu_id=menu_id)
            except Exception as e:
                print('An error occurred uploading file to S3')
                print(e)
        
        return response


class MenuUpdate(UpdateView):
    model = Menu
    form_class = MenuForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu = self.get_object()
        context['photos'] = menu.photos.all()
        return context
    
    def get_success_url(self):
        menu = self.get_object()
        menus = Menu.objects.all().order_by('-id')

        position = list(menus).index(menu) + 1

        
        return f"{reverse('menu')}#{position}"


class MenuDelete(DeleteView):
    model = Menu
    def get_success_url(self):
        return reverse_lazy('menu')

@login_required
def add_photo(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    
    if menu.photos.exists():
        menu.photos.all().delete()

    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, menu=menu)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
            
    return HttpResponseRedirect(reverse('menu_update', args=[menu_id]))


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)