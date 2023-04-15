# Settings
------
#### 1. Database : MySQL
#### 2. Cache
#### 3. Logging
#### 4. TimeZone : Korea
#### 5. Static
#### 6. Templates
#### 7. Connect AWS S3
----
### 1. Database
    pymysql.install_as_MySQLdb()
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "{DATABASE_NAME}",
            "USER": "{DATABASE_USER}",
            "PASSWORD": "{DATABASE_PASSWORD}",
            "HOST": "{DATABASE_HOST}",
            "PORT": "3306",
            "OPTIONS": {
                "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
                "charset": "utf8mb4",
            },
        }
    }

### 2. Cache
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "{CACHE_LOCATION}",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "SERIALIZER": "django_redis.serializers.json.JSONSerializer",
            },
        },
    }

### 3. Logging
**3-1. DEBUG, Tracking sql query**
<!-- <br/> -->
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "format": {"format": "%(message)s"},
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "format",
            }
        },
        "loggers": {
            "django.db.backends": {
                "handlers": ["console"],
                "level": "DEBUG",
            },
        },
    }
**3-2. Basic Api Logging**
<!-- <br/> -->
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "format1": {
                "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                "datefmt": "%d/%b/%Y %H:%M:%S",
            },
            "format2": {"format": "%(levelname)s %(message)s"},
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "format1",
            }
        },
        "loggers": {
            "api": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False,
            },
        },
    }

### 4. TimeZone : Korea
    LANGUAGE_CODE = "ko"
    TIME_ZONE = "Asia/Seoul"
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
### 5. Static
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static/")
### 6. Templates
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "templates")],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

### 7. Connect AWS S3
    # Since Django refers to the settings file, the variable must be stored in the settings file.
    AWS_ACCESS_KEY_ID = ""
    AWS_SECRET_ACCESS_KEY = ""
    AWS_QUERYSTRING_AUTH = False
    AWS_REGION = "ap-northeast-2"
    AWS_STORAGE_BUCKET_NAME = ""
    # S3 Storages
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
        AWS_STORAGE_BUCKET_NAME,
        AWS_REGION,
    )
    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400",
    }
    MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    S3_CLIENT = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
