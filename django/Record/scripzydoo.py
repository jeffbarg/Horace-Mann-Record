from django.core.management import setup_environ
from Record import settings

setup_environ(settings)

from articles.models import Article, Author

import json

json_data=open('useroo.json')

data = json.load(json_data)

dict = {}

for obj in data:

	user_id = obj['user_id']
	if (user_id in dict):
		usr = dict[user_id]	
	else:
		usr = Author()
		dict[user_id] = usr

	if (obj['meta_key'] == 'first_name'):
		usr.first_name = obj['meta_value']
		print usr

	if (obj['meta_key'] == 'last_name'):
		usr.last_name = obj['meta_value']

for k, v in dict.items():
	v.save()