# accounts/views.py

from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegistroUserForm
from .models import UserProfile


def registro_usuario_view(request):
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = RegistroUserForm(request.POST, request.FILES)

        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor, donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            # E instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(username=username, password=password)
            # Añadimos el email
            user_model.email = email
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
            # Ahora, creamos un objeto UserProfile, aunque no haya incluido
            # una imagen, ya quedara la referencia creada en la db.
            user_profile = UserProfile()
            # Al campo user le asignamos el objeto user_model
            user_profile.user = user_model
            # Por ultimo, guardamos tambien el objeto UserProfile
            user_profile.save()
            # Ahora, redireccionamos a la pagina accounts/registro.html
            # Pero lo hacemos con un redirect.
            return redirect('AsociacionVirtual.registro_ok', kwargs={'username': username})
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        form = RegistroUserForm()
    # Creamos el contexto
    context = {'form': form}
    # Y mostramos los datos
    return render(request, 'registro.html', context)


@login_required
def index_view(request):
    return render(request, '/index.html')


def login_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('AsociacionVirtual.index_view'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('accounts.index'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        mensaje = 'Nombre de usuario o contraseña no valido'
    return render(request, 'index.html', {'mensaje': mensaje})