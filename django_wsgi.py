#!/usr/bin/env python 
# coding: utf-8 

import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('/usr/local/lib/python2.7/site-packages/django')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geeklogistics.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
