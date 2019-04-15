from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ToDo
from django.urls import reverse_lazy

def index(request):
    return HttpResponse("Hello World, You are at ToDo's Portal")

class taskListView(ListView):
    model = ToDo
    template_name = 'todo/home.html'

class taskDetailView(DetailView):
    model = ToDo
    template_name = 'todo/detail.html'
    context_object_name = 'task'

class taskUpdateView(UpdateView):
    model = ToDo
    template_name = 'todo/edit.html'
    fields = '__all__'

class taskDeleteView(DeleteView):
    model = ToDo
    template_name = 'todo/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('home')