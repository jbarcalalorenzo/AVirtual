from django.conf.urls import url

from . import views
#Esquema de url-vista
#Nombre de la app
app_name = 'asociacion'
urlpatterns = [
    url(r'^perfil/', views.IndexView, name='index'),
    url(r'^about/', view=views.AboutView.as_view(), name='about'),
    url(r'^contact/', view=views.ContactView.as_view(), name='contact'),
    url(r'^resumen/', views.get_impagos,name='resumen')
]