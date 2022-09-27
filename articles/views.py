from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Article

# Create your views here.
def article_search_view(request):
    try:
        query = int(request.GET.get("q"))
    except:
        query = None

    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {"object": article_obj}
    return render(request, "articles/search.html", context=context)


@login_required
def article_create_view(request):
    context = {}
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article_obj = Article.objects.create(title=title, content=content)
        context["object"] = article_obj
        context["created"] = True
    return render(request, "articles/create.html", context=context)


def article_detail_view(request, id=None):
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {"object": article_obj}
    return render(request, "articles/detail.html", context=context)
