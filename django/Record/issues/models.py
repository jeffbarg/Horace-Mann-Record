from django.db import models
from django.utils import timezone

# Create your models here.

class Issue(models.Model):
	volume			 = models.IntegerField()
	issue 			 = models.IntegerField()

	printissue 		 = models.FileField('Print Issue', upload_to='printissues', blank = True)

	#Date Fields (Technically optional in admin view.  Should always be set.)

	last_updated	 = models.DateTimeField('Last Updated')
	date_published	 = models.DateTimeField('Date Published')


	#Optional Fields

	def __unicode__(self):
		return u"Volume %i, Issue %i" % (self.volume, self.issue,)
	
	def save(self):
		if not self.id:
			if not self.date_published:
				self.date_published = timezone.now()
		
		self.last_updated = timezone.now()
		super(Issue, self).save()