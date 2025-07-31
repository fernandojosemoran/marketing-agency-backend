from storages.backends.s3boto3 import S3Boto3Storage
import os
import environ

env = environ.Env()
environ.Env.read_env()

# config

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
    }
}


# Third party aws apps

AWS_APPS: list[str] = ['storages']


# Essentials environments

AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID")

AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME: str = os.getenv("AWS_STORAGE_BUCKET_NAME")


# optionals environments

STORAGE_DESTINATION: str = os.getenv("STORAGE_DESTINATION")

AWS_S3_CUSTOM_DOMAIN: str = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

PUBLIC_MEDIA_LOCATION = 'media'

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'

DEFAULT_FILE_STORAGE = 'core.storage_backends.PublicMediaStorage'


AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_LOCATION: str = 'static'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_REGION_NAME = "us-east-2"

# helpers methods


class Destinations():
    def isS3() -> bool:
        return STORAGE_DESTINATION == 'S3'


class PublicMediaStorage(S3Boto3Storage):
    location: str = 'media'
    file_overwrite: bool = False
    default_acl: str = 'public-read'
