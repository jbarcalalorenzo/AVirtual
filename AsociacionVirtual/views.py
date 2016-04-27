from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactUsuarioAnonimoForm, ContactUsuarioLoginForm
from AsociacionVirtual import models
from AsociacionVirtual import tables
# Create your views here.


def IndexView(request):
    return render(request, 'Asociacion/index.html')#Esto sera la vista de la app principal(app:OpenSociety)

def registro_ok_View(request):
    return render(request, 'Asociacion/index.html')#El usuario se logeo correctamente y se redirecciona a la pantlla de su asocicacion

# Creamos la vista
class AboutView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'Asociacion/about.html')

# Creamos una función para el envió de email
# (es muy simple, solo para demostrar como enviar un email)
def send_email_contact(email_usuario, subject, body):
    body = '{} ha enviado un email de contacto\n\n{}\n\n{}'.format(email_usuario, subject, body)
    send_mail(
        subject='Nuevo email de contacto',
        message=body,
        from_email='contact@example.com',
        recipient_list=['usuario@example.com']
    )
class ContactView(generic.FormView):

    template_name = 'Asociacion/contact.html'
    success_url = reverse_lazy('contact')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.form_class = ContactUsuarioLoginForm
        else:
            self.form_class = ContactUsuarioAnonimoForm
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        subject = form.cleaned_data.get('subject')
        body = form.cleaned_data.get('body')
        if self.request.user.is_authenticated():
            email_usuario = self.request.user.email
            send_email_contact(email_usuario, subject, body)
        else:
            email_usuario = form.cleaned_data.get('email')
            send_email_contact(email_usuario, subject, body)
        messages.success(self.request, 'Email enviado con exito')
        return super().form_valid(form)

def get_impagos(request):
    queryset = models.Socio.objects.all()
    table = tables.SocioTable(queryset)
    return render(request, 'Asociacion/summary-info.html', {'table': table})

def get_cuentas(request):
    queryset = models.Cuentas.objects.all()
    table = tables.CuentasTable(queryset)
    return render(request, 'Asociacion/_tesoreria.html', {'table': table})