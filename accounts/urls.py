from django.conf.urls import url

from accounts import views as cuentas_views
from AsociacionVirtual import views as Asociacion_views
urlpatterns = [
    url(r'^$', cuentas_views.login_view, name='accounts.login'),
    url(r'^logout',cuentas_views.logout_view, name='accounts.logout'),
    url(r'^perfil', cuentas_views.index_view, name='accounts.index'),
    url(r'^registro',cuentas_views.registro_usuario_view, name="accounts.registro")
]