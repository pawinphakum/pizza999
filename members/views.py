from django.shortcuts import render
from .models import Customer, Favorite
from django.views.generic import ListView

# Create your views here.
def index(request):
    return render(request, 'members/index.html')


class ListView(ListView):
    template_name = 'members/list.html'
    context_object_name = 'customers'
    model = Customer
