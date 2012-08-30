from issues.models import Issue
from django.contrib import admin

class IssueAdmin(admin.ModelAdmin):

	fieldsets = (
	(None, 
		{ 'fields' : ('volume', 'issue', 'date_published', 'printissue',) }), 
	)

#	filter_vertical = ('authors',)

#	list_display = ('title',)
#	search_fields = ['authors__first_name', 'authors__last_name', 'title']

admin.site.register(Issue, IssueAdmin)
