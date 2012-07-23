from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(User):
	profile_picture   = models.ImageField(upload_to='authors/pictures/', blank = True)
	bio 			  = models.TextField('Author Bio', help_text = 'Enter a short bio.', blank = True)
	
	def __str__(self):
		return self.first_name + " " + self.last_name

class Article(models.Model):
	CATEGORY_CHOICES = (
		('OE', 'Opinions and Editorials'),
		('AE', 'Arts and Entertainment'),
		('AF', 'Autofocus'),
		('FT', 'Features'),
		('FH', 'Features Home Page'),
		('LD', "Lion's Den"),
		('MD', 'Middle Division'),
		('NW', 'News'),
	)
	title 			 = models.CharField('Title', help_text = 'Must be under 140 characters.', max_length=140)
	text 			 = models.TextField('Article Text', help_text = 'Copy and paste Article Text into here, then edit using built-in editor as needed.')
	authors		 	 = models.ManyToManyField(Author)

	category 	 	 = models.CharField('Category', max_length=20, choices = CATEGORY_CHOICES)

	is_featured		 = models.BooleanField('Featured' , help_text = 'Is this article in a featured section?')
	is_published	 = models.BooleanField('Published', help_text = 'Should this article be published immediately?')

	#Date Fields (Technically optional in admin view.  Should always be set.)

	last_updated	 = models.DateTimeField('Last Updated', blank = True)
	date_published	 = models.DateTimeField('Date Published', blank = True)

	#Optional Fields

	featured_image   = models.ImageField(upload_to='featured/image', blank = True)

	def __unicode__(self):
		return self.title