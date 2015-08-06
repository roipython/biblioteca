from django.contrib import admin
from biblioteca.models import Autor, Editor, Libro, Usuario

# Register your models here.

class AutorAdmin(admin.ModelAdmin):
	list_display=('nombre', 'apellidos', 'email')

admin.site.register(Autor, AutorAdmin)
admin.site.register(Editor)
admin.site.register(Libro)
admin.site.register(Usuario)
