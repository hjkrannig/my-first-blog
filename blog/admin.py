from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post) #Registriert wird das Model!!
admin.site.register(Comment)

