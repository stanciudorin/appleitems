from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Article

# Create your views here.


def articles(request):
    """ Display all articles """
    articles = Article.objects.all().order_by('pub_date')
    return render(request, 'articles/articles.html', {'articles': articles})