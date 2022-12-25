from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('blog/',blog, name='blog'),
    path('about/',about, name='about'),

    path('login/',login, name='login'),
    path('register/',register, name='register'),
    path('logout/',logout_view, name='logout'),    
    path('dashboard/', include('blog.urls')),

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
