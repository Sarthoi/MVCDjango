from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
def inicio(request):
     return render (request, "pro1/inicio.html")
 
def cursos(request):
     return render(request, "pro1/cursos.html")

def profesores(request):
     return HttpResponse("Profesores")

def estudiantes(request):
     return HttpResponse("Estudiantes")

def entregables(request):
     return HttpResponse("Entregables")