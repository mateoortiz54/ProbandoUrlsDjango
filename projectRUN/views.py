import datetime
from fileinput import close
from django.shortcuts import render
from django.http import  HttpResponse   
from django.template import Context, Template, context

# Create your views here.
def bienvenido(request):
    return HttpResponse("Bienvenido nuevo usuario")

def bienvenidoRojo(request):
    return HttpResponse("<p style='color: red;'>Bienvenido nuevo usuario</p>")

def calcularEdad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "un Viejo"
        else:
            categoria = "usted es un adulto promedio"    
    else:
        if edad >= 10:
            categoria = "no estas peque pero si te falta edad, crack"
        else:
            categoria = "no sirves para nada"
    
    resultado = "Buenas, tu categoria es %s"%categoria
    return HttpResponse(resultado)

def obtenerMomentoActual(request):
    respuesta = "<h1>La hora actual es: {0}</h1>".format(datetime.datetime.now()) #importamos el datetime, y que es esp del 0 y format
    return HttpResponse(respuesta)

def miPrimeraPlantilla(request):
    #abrimos el documento
    documento = open('C:/Users/mateo/Documents/Documentos Del Sena/sena/python/python-Django/proyectoVersion1/RUN/projectRUN/templates/index.html')
    #leemos el documento
    template = Template(documento.read())
    #cerramos el documento como buena practica
    documento.close()
    #creamos el contexto
    contexto = Context()
    #renderizamos el documento
    nuevoDocumento = template.render(contexto)
    return HttpResponse(nuevoDocumento)
    
def miPrimeraPlantillaParametros(request):
    #mandamos una variable 
    fechita = datetime.datetime.now()
    estadoDeAnimo = "Excelentemente"
    diasDeLaSemana = ["Lunes","Martes","Miercoles", "Sabado"]
    #abrimos el documento
    documento = open('C:/Users/mateo/Documents/Documentos Del Sena/sena/python/python-Django/proyectoVersion1/RUN/projectRUN/templates/indexParametros.html')
    #leemos el documento
    template = Template(documento.read())
    #cerramos el documento como buena practica
    documento.close()
    #creamos el contexto
    contexto = Context({"estadoAnimo": estadoDeAnimo, "fecha": fechita, "diasSemana": diasDeLaSemana})
    #renderizamos el documento
    nuevoDocumento = template.render(contexto)
    return HttpResponse(nuevoDocumento)
    
        