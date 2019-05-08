from django.shortcuts import render
from .models import Customer, Favorite, Pizza, Topping
from django.views.generic import ListView

# Create your views here.
def index(request):
    return render(request, 'members/index.html')


class ListView(ListView):
    template_name = 'members/list.html'
    context_object_name = 'customers'
    model = Customer

class ListM2MView(ListView):
    template_name = 'members/list_m2m.html'
    context_object_name = 'pizzas'
    model = Pizza
