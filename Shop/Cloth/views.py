from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import *

from Cloth.forms import RegisterUserForm
from Cloth.models import Item


class ShopHomePage(ListView):
    model = Item
    template_name = 'index.html'
    allow_empty = False


class ShowItemPage(DetailView):
    model = Item
    template_name = 'item.html'
    slug_url_kwarg = 'item_slug'
    context_object_name = 'item'


class AddItem(CreateView):
    model = Item
    template_name = 'AddAdvert.html'
    context_object_name = 'item'
    fields = '__all__'
    success_url = reverse_lazy('home')


class RegisterUser(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')
