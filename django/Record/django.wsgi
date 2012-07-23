import os, sys

sys.path.append('var/www/record.jeffbarg.com/django')
sys.path.append('/var/www/record.jeffbarg.com/django/Record')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Record.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
