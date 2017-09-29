from django.db import models

class Alumno(models.Model):
		name = models.CharField(max_length=140)
		lastname = models.CharField(max_length=140)

class Profesor(models.Model):
		name = models.CharField(max_length=140)
		lastname = models.CharField(max_length=140)
