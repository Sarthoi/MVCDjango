from django.urls import path
from app1.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
    
]


