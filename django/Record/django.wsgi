import os, sys

sys.path.append('var/www/horacemannrecord.com/django')
sys.path.append('/var/www/horacemannrecord.com/django/Record')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Record.production_settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
