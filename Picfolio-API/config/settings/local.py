from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)
# SECRET_KEY = env('SECRET_KEY',default='5(-34b%k6dq@2+ary-=#!wd8^rcsak3zko7&y5*7ilppgap72!')
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

