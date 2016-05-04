from django.conf.urls import url

from . import views
#Esquema de url-vista
#Nombre de la app
app_name = 'asociacion'
urlpatterns = [
    url(r'^perfil/', views.IndexView, name='index'),
    url(r'^about/', view=views.AboutView.as_view(), name='about'),
    url(r'^contact/', view=views.ContactView.as_view(), name='contact'),
    url(r'^resumen/', views.get_impagos,name='resumen'),
    url(r'^tesoreria/', views.get_cuentas, name='tesoreria'),
    url(r'^buscar/', views.search, name='buscar'),
    url(r'^documentos',view=views.DocsView.as_view(),name='documentos'),
    url(r'^test', views.get_charts,name='test'),
    url(r'^informes(?P<tipo>\w+)/$', views.socios_report, name="informes")
]