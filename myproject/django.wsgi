import os
import sys

path = '/home/cslansing/django_projects/myproject'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
