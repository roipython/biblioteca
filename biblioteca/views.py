# -*- encoding: utf-8 -*-
# Create by Roy
from django.shortcuts import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect


from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext

# envio de mail
from django.core.mail import EmailMessage

#importar modelos DB
from biblioteca.models import Autor, Usuario
# Create your views here.
#importamos session activa

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

#importando formularios
from biblioteca.forms import Autor_Update


#variables globales

user = None


@login_required(login_url='/auth_view')
def register(request):
	c={}
	c.update(csrf(request))
	return render_to_response('register.html', c)


@login_required(login_url='/auth_view')
def listar_autor(request):
	autors = Autor.objects.all()
	return render_to_response("autor.html", {"autors":autors})

def inicio(request):
	return render(request, "login.html")

@login_required(login_url='/auth_view')
def home(request):
	return render_to_response('home.html', {'user': request.user}, context_instance=RequestContext(request))


	#c={}
	#c.update(csrf(request))
	#return render_to_response("home.html", c)


def auth_view(request):

	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		if user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect('/home/')


		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')


def register_user(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/register_success')
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	return render_to_response('register_user.html', args)

def register_success(request):
	return	render_to_response('register_success.html')


@login_required(login_url='/auth_view')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')

##################CRUD

@login_required(login_url='/auth_view')
def buscar_autor(request):

	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			#return HttpResponse('Por favor introduce termino de busqueda. XS.')
			autors = Autor.objects.filter()
			return render(request, 'resultado_autor.html', {'autors':autors, 'query':q})
		else:
			autors = Autor.objects.filter(nombre__icontains=q) or Autor.objects.filter(apellidos__icontains=q)
			return render(request, 'resultado_autor.html', {'autors':autors, 'query':q})
	return render(request, 'buscar_autor.html', {'errors':errors})



@login_required(login_url='/auth_view')
def register_autor(request):
	if request.method == 'POST':
		if request.POST['nombre']!= "":
			nombre = request.POST['nombre']
		else:
			return HttpResponse('Por favor introduce los nombre del usuario. XS.')

		if request.POST['apellidos']!= "":
			apellidos = request.POST['apellidos']
		else:
			return HttpResponse('Por favor introduce los apellidos del usuario. XS.')

		if request.POST['email']!= "":
			email = request.POST['email']
		else:
			return HttpResponse('Por favor introduce los email del usuario. XS.')
		autor = Autor(
		nombre=nombre,
		apellidos=apellidos,
		email=email
		)
		autor.save()

	return HttpResponseRedirect('/autores/')

@login_required(login_url='/auth_view')
def delete_autor(request, id):
	Autor.objects.get(id=id).delete()
	return HttpResponseRedirect('/autores/')




@login_required(login_url='/auth_view')
def updateAutor(request, id):

	if request.method == 'GET':
		formulario = Autor_Update(request.GET)
		if formulario.is_valid():
			autor=Autor.objects.get(id=id)
			autor.nombre=request.GET['nombre']
			autor.apellidos = request.GET['apellidos']
			autor.email = request.GET['email']
			autor.save()
			return HttpResponseRedirect('/autores/')
	else:
		formulario=Autor_Update()

	##  Agarra formulario: de esta manera agarramos el formulario para ponerle css en POST
	#args = {}
	#args.update(csrf(request))
	#args['formulario'] = UserCreationForm()"""

	autors = Autor.objects.filter(id=id)
	#return HttpResponse(autors)
	return render_to_response('updateAutor.html', {'autor':autors})
	#return render(request, 'updateAutor.html', args)

print "hola mundo"
