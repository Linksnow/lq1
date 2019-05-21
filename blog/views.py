from django.shortcuts import render
#from django.contrib.auth.models import User
from .models import BlogArticles

def blog_article(request, article_id):
    article=BlogArticles.objects.get(id=article_id)
    pub=article.publish
    return render(request, 'blog/content.html', {"article":article, "publish":pub})
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,'blog/titles.html',{"blogs":blogs})

# Create your views here.
