from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,
                                    RedirectView,UpdateView,DeleteView)
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'validate_car/index.html'

class CarListView(ListView):
    model = models.Car

class DriverListView(ListView):
    model = models.Driver

class DriverDetailView(DetailView):
    model = models.Driver

class CarDetailView(DetailView):
    model = models.Car
