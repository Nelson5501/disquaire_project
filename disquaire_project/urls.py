from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include('store.urls')),
]






if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
       
       ] + urlpatterns
        
   