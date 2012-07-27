from articles.models import Article, Author
from django.contrib import admin
from django.contrib.auth.models import User

class ArticleAdmin(admin.ModelAdmin):
    filter_vertical = ('authors',)
	#inlines = [ArticleTagInline]
    class Media:

		js = ('js/tiny_mce/tiny_mce.js',
			 'js/appmedia/textareas.js',)
	
	
class AuthorAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, 
			{ 'fields' : ('username', 'first_name', 'last_name',) }), 
		('Optional Info',
			{'fields' : ('bio', 'profile_picture'),
			 'classes': ('collapse',),}),
		)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
