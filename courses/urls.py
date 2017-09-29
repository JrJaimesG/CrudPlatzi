from django.conf.urls import url

from .views import (
    AlumnoList,
    AlumnoDetail,
    AlumnoCreation,
    AlumnoUpdate,
    AlumnoDelete,
    ProfesorList,
    ProfesorDetail,
    ProfesorCreation,
    ProfesorUpdate,
    ProfesorDelete
)

urlpatterns = [

    url(r'^$', AlumnoList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', AlumnoDetail.as_view(), name='detail'),
    url(r'^nuevo$', AlumnoCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', AlumnoUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', AlumnoDelete.as_view(), name='delete'),
    
    url(r'^$', ProfesorList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', ProfesorDetail.as_view(), name='detail'),
    url(r'^nuevo$', ProfesorCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', ProfesorUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', ProfesorDelete.as_view(), name='delete'),

]