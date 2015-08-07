from django.db import models

# Create your models here.

class Editor(models.Model):
	nombre = models.CharField(max_length=30)
	domicilio = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=60)
	estado = models.CharField(max_length=30)
	pais = models.CharField(max_length=50)
	website = models.URLField()

class Autor(models.Model):
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=40)
	email = models.EmailField()

	def __str__(self):
		return '%d %s %s %s'%(self.id, self.nombre, self.apellidos, self.email)

class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	autores = models.ManyToManyField(Autor)
	editor = models.ForeignKey(Editor)
	fecha_publicacion = models.DateField()
	portada = models.ImageField(upload_to='portadas')

class Usuario(models.Model):
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
	

    def __str__(self):
        return '%d %s %s %s %s'%(self.id, self.usuario, self.password, self.apellido, self.email)

