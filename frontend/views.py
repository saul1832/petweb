import requests
from django.shortcuts import render


# Create your views here.


def index(request):

    r = requests.get('http://127.0.0.1:8000/api/v1/animal/', auth=('alumno', 'Demo-1234'))
    animales = r.json()
    r = requests.get('http://127.0.0.1:8000/api/v1/diagnostico/', auth=('alumno', 'Demo-1234'))
    diagnosticos = r.json()
    r = requests.get('http://127.0.0.1:8000/api/v1/historial/', auth=('alumno', 'Demo-1234'))
    historiales = r.json()
    r = requests.get('http://127.0.0.1:8000/api/v1/paciente/', auth=('alumno', 'Demo-1234'))
    pacientes = r.json()
    r = requests.get('http://127.0.0.1:8000/api/v1/raza/', auth=('alumno', 'Demo-1234'))
    razas = r.json()

    ctx = {'object_list': animales, 'lista_diagnosticos': diagnosticos, 'lista_historiales': historiales, 'lista_pacientes': pacientes, 'lista_razas': razas}
    return render(request, 'index.html', ctx)
