from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.


def IndexView(request):
    return render(request, 'base.html')#Esto sera la vista de la app principal(app:OpenSociety)

def registro_ok_View(request):
    return render(request, 'AsociacinVirtual/index.html')#El usuario se logeo correctamente y se redirecciona a la pantlla de su asocicacion