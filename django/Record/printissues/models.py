from django.db import models
from django.contrib.auth.models import User
import datetime
from django.template.defaultfilters import slugify

# Create your models here.

class PrintIssue(models.Model):

	#Date Fields (Technically optional in admin view.  Should always be set.)
	volume			 = models.IntegerField()
	issue 			 = models.IntegerField()

	file 			 = models.FileField(upload_to= "printissues")

	last_updated	 = models.DateTimeField('Last Updated', blank = True)
	date_published	 = models.DateTimeField('Date Published', blank = True)

oped_articles = articleobjects.filter(category = "OE").order_by('-date_published')[:1]
	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return "/articles/%s/" % self.slug

	def save(self):
		if not self.id:
			self.slug = slugify(self.title)
			self.date_published = datetime.datetime.today()
		self.last_updated = datetime.datetime.today()
		super(Article, self).save()