# Create your views here.
from django.template import RequestContext, loader
from issues.models import Issue
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.utils import timezone

# Create your views here.

def latest(request):
	issue = Issue.objects.exclude(printissue = '').order_by('-volume', '-issue')[:1].all()[0]

	# authors = article.authors.all

	return detail(request, issue.volume, issue.issue)	
	# t = loader.get_template('printissues/detail.html')
	# c = RequestContext(request, {
	# 	'issue': issue,
	# 	})

	# return HttpResponse(t.render(c))

def archive(request):
	issues = Issue.objects.exclude(printissue = '').order_by('-volume', '-issue')
	
	t = loader.get_template('printissues/archive.html')
	c = RequestContext(request, {
		'issues': issues,
		})

	return HttpResponse(t.render(c))

def detail(request, volume, issue):
	issue = get_object_or_404(Issue, volume=volume, issue=issue)

	# authors = article.authors.all

	return HttpResponseRedirect(issue.printissue.url)	
	# t = loader.get_template('printissues/detail.html')
	# c = RequestContext(request, {
	# 	'issue': issue,
	# 	})

	# return HttpResponse(t.render(c))
