from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lvi%rp_=%a67ig8*%!)%tt$_++9qvel7^q0zl@xu%a-+u$3r91'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    'api.apps.ApiConfig',
]

MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # new
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'

# Конфигурация базы данных
#v1
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',  # Указываем, что используем PostgreSQL
         'NAME': os.getenv('DB_NAME', 'onlinemenudb'),
         'USER': os.getenv('DB_USER', 'postgres'),
         'PASSWORD': os.getenv('DB_PASSWORD', 'online_menu2024'),
         'HOST': os.getenv('DB_HOST', 'online_menu_db'),  # В Docker укажите 'db', как в docker-compose.yml
         'PORT': os.getenv('DB_PORT', '5432'),
     }
}

#v2
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',  # Указываем, что используем PostgreSQL
#        'NAME': os.getenv('DB_NAME', 'armutmenudb'),
#        'USER': os.getenv('DB_USER', 'postgres'),
#        'PASSWORD': os.getenv('DB_PASSWORD', 'armutmenu2024'),
#        'HOST': os.getenv('DB_HOST', 'armut_api_db'),  # В Docker укажите 'db', как в docker-compose.yml
#        'PORT': os.getenv('DB_PORT', '5432'),
#    }
#}

#v3
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',  # Указываем, что используем PostgreSQL
#        'NAME': os.getenv('DB_NAME', 'mervemenudb'),
#        'USER': os.getenv('DB_USER', 'postgres'),
#        'PASSWORD': os.getenv('DB_PASSWORD', 'mervemenu2024'),
#        'HOST': os.getenv('DB_HOST', 'merve_api_db'),  # В Docker укажите 'db', как в docker-compose.yml
#        'PORT': os.getenv('DB_PORT', '5432'),
#    }
#}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

CSRF_TRUSTED_ORIGINS = [
     #"https://merve-api.softclub.tj",
     "https://menu-api.softclub.tj",
]

# CORS_ALLOWED_ORIGINS = [
#     # testing env
#     "http://0.0.0.0:8000",
#     "http://localhost:8000",
#     "http://127.0.0.1:8000",
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
#     "http://37.27.29.18:8000",
# ]

CORS_ALLOW_ALL_ORIGINS = True


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
    ('tj', 'Tajik'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
