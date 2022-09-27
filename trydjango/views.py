from django.shortcuts import render
from articles.models import Article


def home_view(request):
    article_queryset = Article.objects.all()
    context = {"object_list": article_queryset}
    return render(request, "home-view.html", context=context)
