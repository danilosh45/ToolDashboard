
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from news.views import scrape


urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('notepad.urls', namespace='notes')),
    path('scrape', scrape, name='scrape')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

