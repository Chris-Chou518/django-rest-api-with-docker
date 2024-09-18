from .base import * # noqa 
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="bZMuJfyvDhQyZZLzknnKsHqv34JiH7MW2msjZztafbNXaf2czPE",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"] #Django 中用來定義信任的來源域名的設置，專門用來允許特定來源的網站進行跨站請求偽造（CSRF, Cross-Site Request Forgery）保護下的安全請求。

EMAIL_BACKEND="djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST=env("EMAIL_HOST", default="mailhog")
EMAIL_PORT=env("EMAIL_PORT")
DEFAULT_FROM_EMAIL="support@apiimperfect.site"
DOMAIN=env("DOMAIN")
SITE_NAME= "Authors Haven"