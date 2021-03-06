# Copyright 2012 Rooter Analysis S.L.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Django settings for moocng project.

import os
BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

FFMPEG_DEBUG = DEBUG

ADMINS = (
    ('Admin', 'admin@eopenmooc.org'),
)

MANAGERS = ADMINS

EMAIL_SUBJECT_PREFIX = '[OpenMOOC] | '

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'moocng',                # Or path to database file if using sqlite3.
        'USER': 'moocng',                # Not used with sqlite3.
        'PASSWORD': 'moocng',            # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MONGODB_URI = 'mongodb://localhost:27017/moocng'

BADGES_SERVICE_URL = "backpack.openbadges.org"
BADGES_ISSUER_NAME = "OpenMOOC"
BADGES_ISSUER_URL = "http://openmooc.org"
BADGES_ISSUER_DESCRIPTION = ""
BADGES_ISSUER_IMAGE = ""
BADGES_ISSUER_EMAIL = ""

# Tastypie resource limit per page, 0 means unlimited
API_LIMIT_PER_PAGE = 0

#SMTP server
EMAIL_HOST = 'idp.openmooc.org'
SERVER_EMAIL = 'idp.openmooc.org'
DEFAULT_FROM_EMAIL = 'info@openmooc.org'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

EMAIL_SUBJECT_PREFIX = '[OpenMOOC] | '

# Amazon credentials
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_STORAGE_BUCKET_NAME = ""
AWS_S3_UPLOAD_EXPIRE_TIME = (60 * 5)  # 5 minutes

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

gettext = lambda s: s

LANGUAGES = (
    ('en', gettext('English')),
    ('es', gettext('Spanish')),
)

# the default value is 'django_language' but changing this
# to 'language' makes it easier to integrate with the IdP
LANGUAGE_COOKIE_NAME = 'language'

LOCALE_PATHS = (
    os.path.join(BASEDIR, 'locale'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# Use custom formats
FORMAT_MODULE_PATH = 'moocng.formats'

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASEDIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASEDIR, 'collected_static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASEDIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'r$=%l$j4(#5a%$rd*g+q5o7!m3z&amp;b@z1+n*d!n2im-hf0n%730'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'moocng.portal.middleware.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'moocng.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'moocng.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASEDIR, 'templates'),
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

COMPRESS_OFFLINE = False


# This section describes the installed applications for OpenMOOC, it's splitted
# into three for the sake of clarity and usefulness when processing locales
# and application dependant stuff.

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
]

THIRDPARTY_APPS = [
    'grappelli',
    'django.contrib.admin',  # This has to be here because of Grappelli
    'adminsortable',
    'djcelery',
    'tinymce',
    'tastypie',
    'compressor',
    'south',
    'django_mathjax',
]

OPENMOOC_APPS = [
    'moocng.contact',
    'moocng.badges',  # this must be defined before moocng.courses
    'moocng.courses',
    'moocng.assets',
    'moocng.portal',
    'moocng.videos',
    'moocng.teacheradmin',
    'moocng.enrollment',
    'moocng.api',
    'moocng.categories',
    'moocng.auth_handlers',
    'moocng.peerreview',
    'moocng.media_contents',
    'moocng.externalapps',
]

INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + OPENMOOC_APPS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'moocng.videos.download': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'moocng.videos.tasks': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'moocng.courses.admin': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'moocng.externalapps.registry': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    # 'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'moocng.context_processors.site',
    'moocng.context_processors.theme',
    'moocng.context_processors.extra_settings',
    'moocng.context_processors.google_analytics',
    'moocng.context_processors.certificate_url',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'moocng.courses.backends.Saml2BackendExtension',
)

FIXTURE_DIRS = (
    os.path.join(BASEDIR, 'fixtures', 'django.contrib.flatpages'),
    os.path.join(BASEDIR, 'fixtures', 'django.contrib.auth'),
)

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_buttons1': 'bold,italic,underline,strikethrough,separator,link,unlink,separator,undo,redo,copy,paste,separator,cleanup,separator,bullist,numlist',
    'theme_advanced_buttons2': '',
    'theme_advanced_buttons3': '',
}

GOOGLE_ANALYTICS_CODE = ''

GRAVATAR_URL_PREFIX = '//www.gravatar.com/'

MOOCNG_THEME = {
#    'logo': u'',
#    'subtitle': u'',
#    'top_banner': u'',
#    'right_banner1': u'',
#    'right_banner2': u'',
#    'bootstrap_css': u'',
#    'moocng_css': u'',
#    'cert_banner': u'',
}

ENABLED_COMUNICATIONS = (
    'feedback',
    'incidence',
    'rights',
    'unsubscribe',
    'others'
)

#SHOW_TOS = True

FFMPEG = '/usr/bin/ffmpeg'

# Let authenticated users create their own courses
ALLOW_PUBLIC_COURSE_CREATION = False

# A list with the slugs of the courses that use the old qualification system
# where the normal units counted
COURSES_USING_OLD_TRANSCRIPT = []

# Enrollment methods
ENROLLMENT_METHODS = (
    'moocng.enrollment.methods.FreeEnrollment',
)

# Celery settings
import djcelery
djcelery.setup_loader()
CELERY_CREATE_MISSING_QUEUES = True

BROKER_URL = 'amqp://moocng:moocngpassword@localhost:5672/moocng'

CERTIFICATE_URL = 'http://example.com/idcourse/%(courseid)s/email/%(email)s'  # Example, to be overwritten in local settings

MASSIVE_EMAIL_BATCH_SIZE = 30

PEER_REVIEW_TEXT_MAX_SIZE = 5000  # in chars
PEER_REVIEW_FILE_MAX_SIZE = 5  # in MB
PEER_REVIEW_ASSIGNATION_EXPIRE = 24  # in hours

ASSET_SLOT_GRANULARITY = 5  # Slot time of assets should be a multiple of this value (in minutes)

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

FREE_ENROLLMENT_CONSISTENT = False

AUTH_HANDLER = "moocng.auth_handlers.handlers.SAML2"
INSTALLED_APPS.append('djangosaml2')
REGISTRY_URL = 'https://idp.openmooc.org/simplesaml/module.php/userregistration/newUser.php'
PROFILE_URL = 'https://idp.openmooc.org/simplesaml/module.php/userregistration/reviewUser.php'
CHANGEPW_URL = 'https://idp.openmooc.org/simplesaml/module.php/userregistration/changePassword.php'

from .saml_settings import *

### Example config for moocng.auth_handlers.handlers.DBAuth Auth Handler
# INSTALLED_APPS.append('moocng.auth_handlers.dbauth')
# INSTALLED_APPS.append('registration')
# ACCOUNT_ACTIVATION_DAYS = 15

MEDIA_CONTENT_TYPES = [
    {
        'id': 'youtube',
        'name': 'YouTube',
        'handler': 'moocng.media_contents.handlers.youtube.YoutubeMediaContentHandler',
        'can_get_last_frame': True,
    },
    {
        'id': 'vimeo',
        'name': 'Vimeo',
        'handler': 'moocng.media_contents.handlers.vimeo.VimeoMediaContentHandler',
        'can_get_last_frame': False,
    },
    {
        'id': 'scribd',
        'name': 'Scribd',
        'handler': 'moocng.media_contents.handlers.scribd.ScribdMediaContentHandler',
        'can_get_last_frame': False,
    },
    {
        'id': 'prezi',
        'name': 'Prezi',
        'handler': 'moocng.media_contents.handlers.prezi.PreziMediaContentHandler',
        'can_get_last_frame': False,
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
}

MATHJAX_ENABLED = False
MATHJAX_LOCAL_PATH = STATIC_URL + 'js/libs/mathjax'
MATHJAX_CONFIG_FILE = "TeX-AMS-MML_HTMLorMML"
MATHJAX_CONFIG_DATA = {
    "elements": ['false-id-to-not-proccess-by-default'],
    "tex2jax": {
        "inlineMath": [
            ['$', '$'],
            ['\\(', '\\)']
        ]
    }
}


SERIALIZATION_MODULES = {
    "xml": "deep_serializer.serializers.xml_serializer",
    "python": "deep_serializer.serializers.python",
    "json": "deep_serializer.serializers.json",
}

# External apps available to the teachers
# instances is a tuple with the format:
#  (ip, base_url, max_instances,)
#
# Example:
#  MOOCNG_EXTERNALAPPS = {
#     'askbot': {
#         'instances':(
#             ('127.0.0.1', 'http://localhost', 10),
#             ('127.0.0.2', 'http://localhost', 10),
#             ('127.0.0.3', 'http://localhost', 10),
#         )
#     },
#     'wordpress': {
#         'instances':(
#             ('127.0.0.4', 'http://localhost', 10),
#             ('127.0.0.5', 'http://localhost', 10),
#             ('127.0.0.6', 'http://localhost', 10),
#         )
#     }
# }

MOOCNG_EXTERNALAPPS = {
    'askbot': {
        'instances': ()
    },
}

# This settting is a tuple of strings that are not allowed for the slug in the
# external apps. For example:
#
# MOOCNG_EXTERNALAPPS_FORBIDDEN_WORDS = ('word1', 'word2',)
MOOCNG_EXTERNALAPPS_FORBIDDEN_WORDS = ()

# User for fabric tasks execution
FABRIC_TASK_USER = 'root'

# Path where the instances are created. It is used to check if already exists
# an instance on the server
FABRIC_ASKBOT_INSTANCES_PATH = '/etc/openmooc/askbot/instances'

# Path to the ssh key to use to connect to the machines where the external apps
# are going to be deployed
FABRIC_SSH_KEY_PATH = '/root/.ssh/id_rsa'

# Show courses as a list (classic behaviour) or as a grid
COURSE_SHOW_AS_LIST = True
