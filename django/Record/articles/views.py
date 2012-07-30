# Create your views here.
from django.template import RequestContext, loader
from articles.models import Article
from articles.models import Author
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404


def index(request):
	articleobjects = Article.objects

	oped_articles = articleobjects.filter(category = "OE").order_by('-date_published')[:2]
	arts_articles = articleobjects.filter(category = "AE").order_by('-date_published')[:2]
	lionsden_articles = articleobjects.filter(category = "LD").order_by('-date_published')[:2]
	middledivision_articles = articleobjects.filter(category = "MD").order_by('-date_published')[:2]
	news_articles = articleobjects.filter(category = "NW").order_by('-date_published')[:2]
	features_articles = articleobjects.filter(category = "FT").order_by('-date_published')[:2]

	image_articles = articleobjects.exclude(featured_image = '').order_by('-date_published')[:5]

	t = loader.get_template('articles/index.html')
	c = RequestContext(request, {
        'oped_articles': oped_articles,
        'arts_articles': arts_articles,
        'news_articles': news_articles,
        'features_articles':features_articles,
        'lionsden_articles':lionsden_articles,
        'middledivision_articles':middledivision_articles,
        'image_articles':image_articles,
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

def section(request, section):
	CATEGORY_CHOICES = {
		'opeds': 'OE',
		'arts': 'AE',
		'features': 'FT',
		'lionsden': "LD",
		'middledivision': 'MD',
		'news': 'NW',
		}
	if section not in CATEGORY_CHOICES:
		raise Http404
	category = CATEGORY_CHOICES[section]

	verbose_categories = {
		'OE': "Opinions & Editorials",
		'AE': "Arts & Entertainment",
		'FT': "Features",
		'LD': "Lion's Den",
		'MD': "Middle Division",
		'NW': "News",
	}

	articles = Article.objects.filter(category = category).order_by('-date_published')[:10]

	t = loader.get_template('articles/section_index.html')
	c = RequestContext(request, {
        'articles': articles,
        'category': verbose_categories[category],
    })

	return HttpResponse(t.render(c))
