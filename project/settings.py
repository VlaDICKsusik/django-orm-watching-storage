import os
from environs import Env

env = Env()
env.read_env()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
        "NAME": os.environ.get("DB_NAME"),
        "USER":  os.environ.get("DB_USER"),
        "PASSWORD":  os.environ.get("DB_PASSWORD"),
    }
}

INSTALLED_APPS = ["datacenter"]

SECRET_KEY = env.str("SECRET_KEY", "REPLACE_ME")
DEBUG =  env.bool("DEBUG", "True")

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS= os.getenv("ALLOWED_HOSTS")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
    },
]


USE_L10N = True

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
