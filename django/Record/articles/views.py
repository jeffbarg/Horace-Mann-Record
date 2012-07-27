# Create your views here.
from django.template import Context, loader
from articles.models import Article
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    latest_article_list = Article.objects.all().order_by('-date_published')[:5]
    t = loader.get_template('index.html')
    c = Context({
        'latest_article_list': latest_article_list,
    })
    return HttpResponse(t.render(c))
  
def detail(request, article_id):
	p = get_object_or_404(Article, pk=article_id)
	return HttpResponse("You're looking at article %s." % p.text)