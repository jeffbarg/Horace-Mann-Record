from articles.models import Article, Author
from django.contrib import admin
from django.contrib.auth.models import User

class ArticleAdmin(admin.ModelAdmin):
   	filter_vertical = ('authors',)
	#inlines = [ArticleTagInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
