# Create your views here.
from django.template import RequestContext, loader
from articles.models import Article
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    latest_article_list = Article.objects.all().order_by('-date_published')[:5]
    t = loader.get_template('articles/index.html')
    c = RequestContext(request, {
        'latest_article_list': latest_article_list,
    })
    return HttpResponse(t.render(c))
  
def detail(request, article_slug):
	article = get_object_or_404(Article, slug = article_slug)
	# authors = article.authors.all
	
	t = loader.get_template('articles/detail.html')
	c = RequestContext(request, {
		'article': article,
		})
	return HttpResponse(t.render(c))