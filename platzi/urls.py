from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^admin/', admin.site.urls),
]