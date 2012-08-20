from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.
class Author(User):
	profile_picture   = models.ImageField(upload_to='authors/pictures/', blank = True)
	bio 			  = models.TextField('Author Bio', help_text = 'Enter a short bio.', blank = True)
	
	def __unicode__(self):
		return self.first_name + " " + self.last_name



	def save(self):
		if not self.id:
			uname = "%s%s" % (self.first_name, self.last_name)
			while (len(Author.objects.filter(username = uname)) > 0):
				uname = "%s%s" % (uname, "_")

			self.username = uname
		super(Author, self).save()

class Article(models.Model):
	CATEGORY_CHOICES = (
		('OE', 'Opinions and Editorials'),
		('AE', 'Arts and Entertainment'),
		('FT', 'Features'),
		('LD', "Lion's Den"),
		('MD', 'Middle Division'),
		('NW', 'News'),
	)
	title 			 = models.CharField('Title', help_text = 'Must be under 140 characters.', max_length=140)
	text 			 = models.TextField('Article Text', help_text = 'Copy and paste Article Text into here, then edit using built-in editor as needed.')
	authors		 	 = models.ManyToManyField(Author, related_name='articles')

	slug 			 = models.SlugField('Slug', max_length = 150, blank = True)

	category 	 	 = models.CharField('Category', max_length=20, choices = CATEGORY_CHOICES)

	is_featured		 = models.BooleanField('Featured' , help_text = 'Is this article in a featured section?')

	#Date Fields (Technically optional in admin view.  Should always be set.)

	last_updated	 = models.DateTimeField('Last Updated', blank = True)
	date_published	 = models.DateTimeField('Date Published', blank = True)

	#Optional Fields

	featured_image   = models.ImageField(upload_to='featured/image', blank = True)

	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return "/articles/%s/" % self.slug

	def save(self):
		if not self.id:
			if not self.slug:
				self.slug = slugify(self.title)
			if not self.date_published:
				self.date_published = timezone.now()
		
		self.last_updated = timezone.now()
		super(Article, self).save()
