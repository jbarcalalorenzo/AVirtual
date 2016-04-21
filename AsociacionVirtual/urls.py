from django.conf.urls import url

from . import views
#Esquema de url-vista
#Nombre de la app
app_name = 'asociacion'
urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
]