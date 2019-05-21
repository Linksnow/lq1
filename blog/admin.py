from django.contrib import admin
from .models import BlogArticles

#将该类注册到admin中

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title","publish","author")
    list_filter = ("publish","author")
    search_fields = ("title","body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ['publish','author']

admin.site.register(BlogArticles,BlogArticlesAdmin)
# Register your models here.
