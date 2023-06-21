from django.http import HttpResponse
from django.template import loader
from app1.models import Curso


def saludo(request):
    return HttpResponse("Hello")


def seg_vista(request):
    return HttpResponse("<br></br> <h1>Jelou Madafaka :D</h1>")


def nombre(self, name):
    data = f"Mi nombre es <h1>{name}</h1>"
    return HttpResponse(data)


def template_uno(self):
    nombre = "Sadrac"
    apellido = "Araneda"

    namelist = ["Tauma", "Zapatito", "Botita", "Rocky"]

    diccionario = {"nombre": nombre,
                   "apellido": apellido,
                   "lista": namelist 
                }

    plantilla=loader.get_template("index.html")
    document = plantilla.render(diccionario)
    return HttpResponse(document)

def curso(self):
    curso= Curso(nombre="Python", camada="54485")
    curso.save()
    documentxt = f"--->Curso:{curso.nombre}  Camada: {curso.camada}"
    return HttpResponse(documentxt)