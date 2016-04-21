from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registro/$', views.registro_usuario_view, name='accounts.registro'),
]