from django.contrib import admin
from django.urls import path, include
# next two for media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booksite.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
