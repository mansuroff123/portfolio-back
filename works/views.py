from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Work

# Create your views here.

class WorkList(ListView):
    model = Work
    template_name = 'main/works.html'
    context_object_name = 'works'

class WorkDetail(DetailView):
    model = Work
    template_name = 'main/work_detail.html'
    context_object_name = 'work'