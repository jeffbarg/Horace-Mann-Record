from django.db import models
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
	
	def __unicode__(self):
		return u"a print issue"

	def get_absolute_url(self):
		return "/articles/%s/" % self.slug

	def save(self):
		if not self.id:
			self.date_published = datetime.datetime.today()
		self.last_updated = datetime.datetime.today()
		super(PrintIssue, self).save()
