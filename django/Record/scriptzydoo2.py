from django.core.management import setup_environ
from Record import settings
from django.utils.timezone import utc

setup_environ(settings)

import dateutil.parser

from articles.models import Article, Author

import json

json_data=open('useroo.json')

data = json.load(json_data)

usr_dict = {}

for obj in data:

	user_id = obj['user_id']
	if (user_id in usr_dict):
		usr = usr_dict[user_id]	
	else:
		usr = Author()
		usr_dict[user_id] = usr

	if (obj['meta_key'] == 'first_name'):
		usr.first_name = obj['meta_value']
		print usr

	if (obj['meta_key'] == 'last_name'):
		usr.last_name = obj['meta_value']

for k, v in usr_dict.items():
	v.save()

post_data=open('posteroo.json')

data = json.load(post_data)

post_dict = {}

for obj in data:
	if (obj['post_status'] != "publish"):
		continue;

	if (len(obj['post_content']) == 0) :
		continue;

	if (len(obj['post_title']) == 0) :
		continue;

	post_id = obj['ID']

	if (post_id in post_dict):
		article = post_dict[post_id]	
	else:
		article = Article()
		post_dict[post_id] = article
	
	article.title = obj['post_title']
	article.save()

	article.date_published = dateutil.parser.parse(obj['post_modified'])
	article.text = "%s%s%s" % ('<p>', obj['post_content'].replace('&nbsp;','').replace('&nbsp;\n','').replace('\n\n', '\n').replace('\n', '</p><p>'), '</p>')

	article.authors.add(usr_dict[obj['post_author']])

for k, v in post_dict.items():
	v.save()

category_data = open('termzeroo.json')
data = json.load(category_data)

for obj in data:
	if (obj['term_taxonomy_id'] == '7') or (obj['term_taxonomy_id'] == '8') or (obj['term_taxonomy_id'] == '9') or (obj['term_taxonomy_id'] == '10'):
		article = post_dict.get(obj['object_id'], None)
		if (article != None):
			article.category = "FT"

	if (obj['term_taxonomy_id'] == '5') or (obj['term_taxonomy_id'] == '6'):
		article = post_dict.get(obj['object_id'], None)
		if (article != None):
			article.category = "AE"

	if (obj['term_taxonomy_id'] == '11') or (obj['term_taxonomy_id'] == '12'):
		article = post_dict.get(obj['object_id'], None)
		if (article != None):
			article.category = "LD"

	if (obj['term_taxonomy_id'] == '13') or (obj['term_taxonomy_id'] == '14'):
		article = post_dict.get(obj['object_id'], None)
		if (article != None):
			article.category = "MD"	

	if (obj['term_taxonomy_id'] == '15') or (obj['term_taxonomy_id'] == '16'):
		article = post_dict.get(obj['object_id'], None)
		if (article != None):
			article.category = "NW"	

	if (obj['term_taxonomy_id'] == '17') or (obj['term_taxonomy_id'] == '18'):
		article = post_dict.get(obj['object_id'], None)
		if (article != None):
			article.category = "OE"	
for k, v in post_dict.items():
	v.save()

