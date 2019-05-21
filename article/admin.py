from django.contrib import admin

from .models import ArticleColumn
from .models import ArticlePost

class ArticleColumnAdmin(admin.ModelAdmin):
    list_display=('column','created','user')
    list_filter=('column',)

admin.site.register(ArticleColumn,ArticleColumnAdmin)

class ArticlePostAdmin(admin.ModelAdmin):
    list_display=('title','body','created','updated','slug','column','author')
    list_filter=('column','author','created','updated',)

admin.site.register(ArticlePost,ArticlePostAdmin)