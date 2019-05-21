from django.urls import path

from . import views
from . import list_views

app_name='article'

urlpatterns=[
    path('article_column/',views.article_column,name='article_column'),
    path('article_post/',views.article_post,name='article_post'),
    path('article_list/',views.article_list,name='article_list'),
    path('article_detail/<id>/<slug>/',views.article_detail,name="article_detail"),
    path('article_titles/',list_views.article_titles,name='article_titles'),
    path('del_article/',views.del_article,name='del_article'),
    path('redit_article/<article_id>',views.redit_article,name='redit_article'),
    path('rename_column/', views.rename_article_column, name="rename_article_column"),
    path('del_column/', views.del_article_column, name="del_article_column"),
]

