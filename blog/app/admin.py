from django.contrib import admin
from .models import Post
# Register your models here.

#mettre plus d'info sur le post dans la partie admin
class PostAdmin(admin.ModelAdmin):
    list_display =('title' , 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']

#On lie la table post à la page admin
admin.site.register(Post, PostAdmin)