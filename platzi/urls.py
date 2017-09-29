from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^alumnos/', include('courses.urls', namespace='alumnos')),
	url(r'^profesores/', include('courses.urls', namespace='profesores')),
	url(r'^admin/', admin.site.urls),
]