from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Diego")

def despedida(request):
    return HttpResponse("<h1>Este es insercion de html</h1>")

def Fecha(request):
    fecha_actual = datetime.datetime.now()

    estructura = """<html>
        <h1> Fecha y hs actual %s </h1>

    </html>   """ %fecha_actual
    return HttpResponse(estructura)

def Pagina(request):
    doc_externo=open(Templates/templates.html)
    plantilla=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plantilla.render(ctx)
    return HttpResponse(documento)
