"""
Django settings for core project.
"""

import os
from pathlib import Path
import dj_database_url
from environ import Env
env = Env()
Env.read_env()
# ENVIRONMENT= env("ENVIRONMENT", default="production")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


IS_PRODUCTION = os.environ.get("RAILWAY_ENV", "development") == "production"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default="unsafe-secret-key-for-build")

# SECRET_KEY = env("SECRET_KEY")

# ENCRYPT_KEY = env("ENCRYPT_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
if ENVIRONMENT == "development":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ["*"]

# ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'localhost:3000','.railway.app','hadi-store.up.railway.app']
CSRF_TRUSTED_ORIGINS = [ 'https://hadi-store.up.railway.app' ]

# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',   
    'corsheaders',
    'products',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# DATABASES = {
#     "default": dj_database_url.config(
#         default="sqlite:///db.sqlite3",
#         conn_max_age=600,
#         ssl_require=IS_PRODUCTION,
#     )
# }
# DATABASES = {
#     'default':{
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# POSTGRES_LOCALLY = False
# if ENVIRONMENT == "production" or POSTGRES_LOCALLY == True:
#     DATABASES['default' ]= dj_database_url.parse(env('DATABASE_URL'))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if os.getenv("DATABASE_URL"):
    DATABASES['default'] = dj_database_url.parse(
        os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
else:
    print("DATABASE_URL missing, using default SQLite")


# Password validation

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


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3001",
    "https://ecommerce-frontend-ten-tawny.vercel.app",
    "https://hadi-store.up.railway.app",
    
]
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True



# if IS_PRODUCTION:
#     CSRF_TRUSTED_ORIGINS = [
#         'https://hadi-store.up.railway.app',
#         'https://ecommerce-frontend-ten-tawny.vercel.app',
#     ]
# else:
#     CSRF_TRUSTED_ORIGINS = [
#         'http://localhost:8000',
#         'http://127.0.0.1:8000',
#         'https://hadi-store.up.railway.app',
#         'https://ecommerce-frontend-ten-tawny.vercel.app',

#     ]

CSRF_COOKIE_SECURE = IS_PRODUCTION
SESSION_COOKIE_SECURE = IS_PRODUCTION

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') if IS_PRODUCTION else None

