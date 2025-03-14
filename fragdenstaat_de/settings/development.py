from .base import FragDenStaatBase, env


class Dev(FragDenStaatBase):
    GEOIP_PATH = None

    CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}

    DATABASES = {
        "default": {
            "ENGINE": "django.contrib.gis.db.backends.postgis",
            "NAME": env("DATABASE_NAME", "fragdenstaat_de"),
            "OPTIONS": {},
            "HOST": "fragdenstaat_de-db-1",
            "USER": env("DATABASE_USER", "fragdenstaat_de"),
            "PASSWORD": env("DATABASE_PASSWORD", "fragdenstaat_de"),
            "PORT": "5432",
        }
    }

    FRONTEND_SERVER_URL = "http://192.168.100.122:5173/static/"

    # INSTALLED_APPS = list(FragDenStaatBase().INSTALLED_APPS) + [
    #     'corsheaders',
    # ]

    # MIDDLEWARE = list(FragDenStaatBase().MIDDLEWARE) + [
    #     'corsheaders.middleware.CorsMiddleware',
    # ]

    # CORS_ALLOWED_ORIGINS = [
    #     "http://0.0.0.0:5173",
    # ]
    # CORS_ORIGIN_ALLOW_ALL = True

    @property
    def TEMPLATES(self):
        TEMP = super().TEMPLATES
        TEMP[0]["OPTIONS"]["debug"] = True
        return TEMP


try:
    from .local_settings import Dev  # noqa
except ImportError:
    pass
