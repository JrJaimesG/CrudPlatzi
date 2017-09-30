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

    url(r'^alumnos$', AlumnoList.as_view(), name='alumnos_list'),
    url(r'^alumnos/(?P<pk>\d+)$', AlumnoDetail.as_view(), name='alumno_detail'),
    url(r'^alumnos/nuevo$', AlumnoCreation.as_view(), name='alumno_new'),
    url(r'^alumnos/editar/(?P<pk>\d+)$', AlumnoUpdate.as_view(), name='alumno_edit'),
    url(r'^alumnos/borrar/(?P<pk>\d+)$', AlumnoDelete.as_view(), name='alumno_delete'),

    url(r'^profesores$', ProfesorList.as_view(), name='profesores_list'),
    url(r'^profesores/(?P<pk>\d+)$', ProfesorDetail.as_view(), name='profesor_detail'),
    url(r'^profesores/nuevo$', ProfesorCreation.as_view(), name='profesor_new'),
    url(r'^profesores/editar/(?P<pk>\d+)$', ProfesorUpdate.as_view(), name='profesor_edit'),
    url(r'^profesoresborrar/(?P<pk>\d+)$', ProfesorDelete.as_view(), name='profesor_delete'),

]