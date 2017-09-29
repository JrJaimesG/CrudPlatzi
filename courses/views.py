from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Alumno, Profesor


class AlumnoList(ListView):
    model = Alumno

class AlumnoDetail(DetailView):
    model = Alumno

class AlumnoCreation(CreateView):
    model = Alumno
    success_url = reverse_lazy('courses:list')
    fields = ['name', 'lastname']


class AlumnoUpdate(UpdateView):
    model = Alumno
    success_url = reverse_lazy('courses:list')
    fields = ['name', 'lastname']


class AlumnoDelete(DeleteView):
    model = Alumno
    success_url = reverse_lazy('courses:list')




class ProfesorList(ListView):
    model = Profesor

class ProfesorDetail(DetailView):
    model = Profesor

class ProfesorCreation(CreateView):
    model = Profesor
    success_url = reverse_lazy('courses:list')
    fields = ['name', 'lastname']


class ProfesorUpdate(UpdateView):
    model = Profesor
    success_url = reverse_lazy('courses:list')
    fields = ['name', 'lastname']


class ProfesorDelete(DeleteView):
    model = Profesor
    success_url = reverse_lazy('courses:list')