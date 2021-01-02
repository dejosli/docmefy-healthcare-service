"""docmefy_healthcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import profile_redirect_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('docmefy.urls')),
    path('accounts/', include('allauth.urls')),
    # path('profiles/', include('users.urls')),
    path('profiles/', profile_redirect_view, name='profile-redirect'),
]

admin.site.site_title = 'Docmefy Admin'
admin.site.site_header = 'Docmefy Administration'
admin.site.index_title = 'DATA BASE ADMINISTRATION'

# By default, Django doesn’t serve media files during development(when debug=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
