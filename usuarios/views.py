from multiprocessing import AuthenticationError, context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from usuarios.forms import UserEditForm, form_profile, form_profile_image
from django.contrib import messages
from usuarios.models import User_profile
from django.contrib.auth.decorators import login_required
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'paginas/inicio.html')
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'error': 'Formulario invalido', 'form':form} )
    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form} )

def register(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        else:
            context = {'errors':form.errors}
            form = UserEditForm()
            context['form'] = form
            return render(request, 'users/register.html', context)

    else:
        form = UserEditForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def Perfil(request):
    try:
        context = {
            'user': request.user.profile.user,
            'phone': request.user.profile.phone,
            'address': request.user.profile.address,
            'image': request.user.profile.image
        }
        return render(request, 'users/profile.html', context=context)
    except:
        User_profile.objects.create(
            user_id = request.user.id
        )
        return render(request, 'users/profile.html')

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password1']
            usuario.save()
            return render(request,'inicio.html')
    else:
        form = UserEditForm(initial={'email':usuario.email} )
    return render(request,'users/editarPerfil.html',{'form':form,'usuario':usuario} )

@login_required
def EditarPerfilImage(request):
        if request.method == 'POST':
            form = form_profile_image(request.POST or None, request.FILES or None)
            if form.is_valid():
                request.user.profile.image = form.cleaned_data['image']
                request.user.profile.save()
                return redirect(Perfil)
        elif request.method == 'GET':
            if request.user.profile.image:
                image = request.user.profile.image
            else:
                image = ''
            form = form_profile_image()     
            context = {
                'form': form,
            'user': request.user.profile.user,
            'phone': request.user.profile.phone,
            'address': request.user.profile.address,
            'image': request.user.profile.profile_image,
        }
            return render(request, 'users/profileEditarimage.html', context=context)



