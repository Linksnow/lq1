from django.urls import path
from .views import blog_title
from .views import blog_article
app_name='blog'
urlpatterns=[
    path('', blog_title, name="blog_title"),
    path('<article_id>',blog_article, name="blog_article")
]