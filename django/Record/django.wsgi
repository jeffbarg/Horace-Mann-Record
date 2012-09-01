import os, sys

sys.path.append('var/www/horacemannrecord.com/django')
sys.path.append('/var/www/horacemannrecord.com/django/Record')
sys.path.append('/usr/local/lib/python2.7/dist-packages/sorl/thumbnail/')
sys.path.append('/usr/local/lib/python2.7/dist-packages/sorl/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Record.production_settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
