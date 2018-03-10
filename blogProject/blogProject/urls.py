from django.conf.urls import include, url
from django.contrib import admin
# from django.urls import path

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # path('admin/', admin.site.urls),
    url(r'^blog/', include("blog.urls", namespace="blog", app_name="blog")),
]