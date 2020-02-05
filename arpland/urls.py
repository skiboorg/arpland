
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    # path('item/', include('item.urls')),
    path('news/', include('blog.urls')),
    path('user/', include('customuser.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
