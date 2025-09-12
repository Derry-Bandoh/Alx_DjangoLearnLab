
from pathlib import Path
import os
from decouple import config, Csv # For environment variable management

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ql3ts@$umd2$jmuz(l^i=1_$wdey4#_j7ox!a&p2tv3&y(%_#@'

# SECURITY WARNING: don't run with debug turned on in production!
# Environment detection
DEBUG = config('DEBUG', default=True, cast=bool)
PRODUCTION = not DEBUG


# ALLOWED_HOSTS = []

# Allowed hosts - configure for both development and production
ALLOWED_HOSTS = config('ALLOWED_HOSTS', 
                      default='localhost,127.0.0.1,0.0.0.0', 
                      cast=Csv())

# Redirect all HTTP requests to HTTPS (only in production)
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=PRODUCTION, cast=bool)

# HTTP Strict Transport Security (HSTS)
# 31536000 seconds = 1 year - only enable in production
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', 
                           default=31536000 if PRODUCTION else 0, 
                           cast=int)

# Include subdomains in HSTS policy
SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', 
                                      default=PRODUCTION, 
                                      cast=bool)

# Allow HSTS preloading (submit your site to browser preload lists)
SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', 
                           default=PRODUCTION, 
                           cast=bool)

# For proxy setups (if using nginx/Apache as reverse proxy)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Only send session cookies over HTTPS
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', 
                             default=PRODUCTION, 
                             cast=bool)

# Only send CSRF cookies over HTTPS
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', 
                          default=PRODUCTION, 
                          cast=bool)
# Prevent JavaScript access to session cookies (always enabled for security)
SESSION_COOKIE_HTTPONLY = True

# Prevent JavaScript access to CSRF cookies
CSRF_COOKIE_HTTPONLY = False  # Usually False to allow JavaScript frameworks

# Session expiration settings
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Session ends when browser closes
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds (optional)

# Prevent clickjacking by denying framing
X_FRAME_OPTIONS = 'DENY'

# Prevent MIME type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser's XSS filter
SECURE_BROWSER_XSS_FILTER = True

# Referrer policy - control how much referrer information is sent
SECURE_REFERRER_POLICY = 'same-origin'



# Application definition

INSTALLED_APPS = [
    'bookshelf.apps.BookshelfConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'relationship_app.apps.RelationshipAppConfig',
     
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
AUTH_USER_MODEL = 'bookshelf.CustomUser'  # Custom user model


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SSL/HTTPS settings (for production)
SECURE_SSL_REDIRECT = True  # Redirect all HTTP to HTTPS
SESSION_COOKIE_SECURE = True  # Only send session cookies over HTTPS
CSRF_COOKIE_SECURE = True  # Only send CSRF cookies over HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # For proxy setups

# Browser security headers
SECURE_BROWSER_XSS_FILTER = True  # Enable XSS filter in browsers
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME type sniffing

# HSTS settings (for production)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Additional security settings
SECURE_REFERRER_POLICY = 'same-origin'  # Control referrer information


CSP_DEFAULT_SRC = ["'self'"]
CSP_SCRIPT_SRC = ["'self'"]
CSP_STYLE_SRC = ["'self'", "'unsafe-inline'"]  # Allow inline styles if needed
CSP_IMG_SRC = ["'self'", "data:"]
CSP_FONT_SRC = ["'self'"]
CSP_OBJECT_SRC = ["'none'"]
CSP_BASE_URI = ["'none'"]
CSP_FORM_ACTION = ["'self'"]


SESSION_COOKIE_HTTPONLY = True  # Prevent JavaScript access to session cookie
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Session expires when browser closes

# File upload security
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10MB max upload
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10MB max file upload
