from datetime import date
from io import BytesIO

from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views import generic

from AsociacionVirtual import models
from AsociacionVirtual import tables
from AsociacionVirtual.report import PdfPrint
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactUsuarioAnonimoForm, ContactUsuarioLoginForm


# Create your views here.


def IndexView(request):
    return render(request, 'Asociacion/index.html')  # Esto sera la vista de la app principal(app:OpenSociety)


def registro_ok_View(request):
    return render(request,
                  'Asociacion/index.html')  # El usuario se logeo correctamente y se redirecciona a la pantlla de su asocicacion


# Creamos la vista
class AboutView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Asociacion/about.html',context_instance=RequestContext(request))


class DocsView(generic.View):
    def get(self, request, *args, **kwargs):
        docs = models.Documentos.objects.all()
        table = tables.DocsTable(docs)
        return render(request, 'Asociacion/documentos.html', {'table': table})


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


def search(request):
    if 'value' in request.GET and request.GET['value']:
        q = request.GET['value']
        socios = models.Documentos.objects.filter(id__icontains=q)
        table = tables.DocsTable(socios)
        return render(request, 'search_results.html', {'table': table, 'query': q})
    else:
        socios = models.Socio.objects.all()
        table = tables.DocsTable(socios)
        return render(request, 'search_results.html', {'table': table})

def socios_report(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        if tipo is not None:
            response = HttpResponse(content_type='application/pdf')
            today = date.today()
            # asociacion = models.Asociacion.objects.all()
            if tipo == 'Socio':
                filename = 'impago_socios' + today.strftime('%Y-%m-%d')
                header = "Impagos de socios"
            if tipo == "Evento":
                filename = 'eventos' + today.strftime('%Y-%m-%d')
                header = "Evento"
            if tipo == "Alquiler":
                filename = 'devoluciones' + today.strftime('%Y-%m-%d')
                header = "Alquiler"
            response['Content-Disposition'] = 'attachement; filename={0}.pdf'.format(filename)
            buffer = BytesIO()
            report = PdfPrint(buffer, 'A4')
            pdf = report.report(header, tipo)
            response.write(pdf)
            return response
        else:  return render(request, 'Asociacion/error.html')
