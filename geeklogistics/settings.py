# coding:utf-8
# -*- coding:utf-8 -*-
"""
Django settings for geeklogistics project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'titww8r+_p*po$rqytl&$z5c_ncp!1im(dno+=a5a!14v_1=_='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

FILE_CHARSET = 'utf-8'
DEFAULT_CHARSET = 'utf-8'

# Application definition
from django.contrib import messages

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'geeklogistics.order',
    'geeklogistics.deliver',
    'geeklogistics.poi',
    'geeklogistics.news',
    'geeklogistics.station',
    'geeklogistics.webapp',
    # 'import_export',
    # 'bootstrapform'
    # 'django.template.loaders.filesystem.Loader',
    # 'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
    # 'django.template.loaders.app_directories.load_template_source',
    # 'geeklogistics.templatetags',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'geeklogistics.urls'

WSGI_APPLICATION = 'geeklogistics.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'geeklogistics',  # 你的数据库名称
        'USER': 'root',  # 你的数据库用户名
        'PASSWORD': 'Gl_123456',  # 你的数据库密码
        'HOST': '',  # 你的数据库主机，留空默认为localhost
        'PORT': '3306',  # 你的数据库端口
        # 'OPTIONS': {'charset': 'utf8mb4'},
    }
}

# admin
# DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'
# MESSAGE_TAGS = {
#     messages.SUCCESS: 'alert-success success',
#     messages.WARNING: 'alert-warning warning',
#     messages.ERROR: 'alert-danger error'
# }
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

SUIT_CONFIG = {
    'ADMIN_NAME': u'极客冷链管理后台',
    'MENU': (
        'sites',
        {'app': 'order', 'label': u'订单管理'},
        {'app': 'deliver', 'label': u'配送员管理'},
        {'app': 'poi', 'label': u'商家管理'},
        {'app': 'news', 'label': u'新闻管理'},
        {'app': 'station', 'label': u'配送点管理'},

    ),
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates').replace('\\', '/'),

)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
M_MEDIA_SITE = 'static/m/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [['CodeSnippet', ], ],
        'height': 400,
        'width': 900,
        'removePlugins': 'stylesheetparser',
        'extraPlugins': 'codesnippet',
    },
}
STATICFILES_DIRS = (
    ("css", os.path.join(STATIC_ROOT, 'css')),
    ("js", os.path.join(STATIC_ROOT, 'js')),
    ("images", os.path.join(STATIC_ROOT, 'images')),
    ("bootstrap", os.path.join(STATIC_ROOT, 'bootstrap')),
    ("ckeditor", os.path.join(STATIC_ROOT, 'ckeditor')),
)

# 这个是默认设置，默认会找 STATICFILES_DIRS 中所有文件夹和各app下的 static 文件夹
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)
STATIC_URL = '/static/'
