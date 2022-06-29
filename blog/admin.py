from django.contrib import admin
from .models import Post

# registrando nosso modelo para torna-lo visivel na pagina de administradir
admin.site.register(Post)
