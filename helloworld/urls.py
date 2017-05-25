from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from hello.view_sets import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, base_name='post')

urlpatterns = [
    # Examples:
    url(r'^$', 'hello.views.home', name='home'),
    url(r'^json_example/$', 'hello.views.json_example', name='json_example'),
    url(r'^post_echo/$', 'hello.views.post_echo', name='post_echo'),
    url(r'^unicode_401/$', 'hello.views.unicode_401', name='unicode_401'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
