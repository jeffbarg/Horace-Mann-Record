from articles.models import Article, Author
from django.contrib import admin
from django.contrib.auth.models import User

class ArticleAdmin(admin.ModelAdmin):

	fieldsets = (
	(None, 
		{ 'fields' : ('title', 'text', 'authors', 'category', 'issue',) }), 
	# ('Optional Info',
	# 	{'fields' : ('block_quote',),
	# 	 'classes': ('wide',),}),
	('Featured Image',
		{'fields' : ('featured_image', 'image_caption'),
		 'classes': ('wide',),}),
	('Home Page Features',
		{'fields' : ('is_featured', 'is_photo_featured'),
		 'classes': ('wide',),}),
	)

	filter_vertical = ('authors',)
	list_display = ('title',)
	search_fields = ['authors__first_name', 'authors__last_name', 'title']
	class Media:

		js = ('js/tiny_mce/tiny_mce.js',
			 'js/appmedia/textareas.js',)
		

	
class AuthorAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, 
			{ 'fields' : ('first_name', 'last_name',) }), 
		('Optional Info',
			{'fields' : ('bio', 'profile_picture'),
			 'classes': ('collapse',),}),
		)
	search_fields = ['first_name', 'last_name', 'username']
	
	list_display = ('get_full_name', 'first_name', 'last_name')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
