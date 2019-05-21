from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .models import ArticlePost,ArticleColumn

def article_titles(request):
    article_title=ArticlePost.objects.all()
    paginater=Paginator(article_title,2)
    page=request.GET.get('page')
    try:
        current_page=paginater.page(page)
        articles=current_page.object_list
    except PageNotAnInteger:
        current_page=paginater.page(1)
        articles=current_page.object_list
    except EmptyPage:
        current_page=paginater.page(paginater.num_pages)
        articles=current_page.object_list
    return render(request,'article/list/article_titles.html',{'articles':articles,'page':current_page})