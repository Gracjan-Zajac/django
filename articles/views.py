from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404

from .forms import ArticleForm
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
    form = ArticleForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        article_obj = form.save()
        context["form"] = ArticleForm()
        # context["object"] = article_obj
        # context["created"] = True
    return render(request, "articles/create.html", context=context)


def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404("Article does not exist")
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {"object": article_obj}
    return render(request, "articles/detail.html", context=context)
