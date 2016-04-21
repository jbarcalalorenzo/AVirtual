from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.


def IndexView(request):
   return render(request,"base.html")