from django.template import RequestContext, loader
from printissues.models import PrintIssue
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404

# Create your views here.

def latest(request):
	issue = PrintIssue.objects.order_by('-volume', '-issue')[:1].all()[0]

	# authors = article.authors.all
	
	t = loader.get_template('printissues/detail.html')
	c = RequestContext(request, {
		'issue': issue,
		})

	return HttpResponse(t.render(c))

def archive(request):
	issues = PrintIssue.objects.order_by('-volume', '-issue')
	
	t = loader.get_template('printissues/archive.html')
	c = RequestContext(request, {
		'issues': issues,
		})

	return HttpResponse(t.render(c))

def detail(request, volume, issue):
	issue = get_object_or_404(PrintIssue, volume=volume, issue=issue)

	# authors = article.authors.all
	
	t = loader.get_template('printissues/detail.html')
	c = RequestContext(request, {
		'issue': issue,
		})

	return HttpResponse(t.render(c))