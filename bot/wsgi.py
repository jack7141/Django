"""
WSGI config for bot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/ubuntu/KakaoChat')
sys.path.append('/home/ubuntu/KakaoChat/bot')
sys.path.append('/home/ubuntu/KakaoChat/myvenv/lib/python3.5/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bot.settings")

application = get_wsgi_application()
