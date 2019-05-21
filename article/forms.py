from django import forms

from .models import ArticleColumn
from .models import ArticlePost

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model=ArticlePost
        fields=("title","body",)


class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model=ArticleColumn
        fields=('column',)