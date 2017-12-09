from django.db import models
from django.contrib.postgres.fields import JSONField

class effect(models.Model):
	name = models.CharField(max_length=20)
	consequences = JSONField()

class skill(models.Model):
	name = models.CharField(max_length=20)
	duration = models.IntegerField()
	effects = models.ManyToManyField(effect)

class breed(models.Model):
	name = models.CharField(max_length=20)
	mean_height = models.FloatField()
	habitat = models.CharField(max_length=20)
	passive_skill = models.ManyToManyField(skill)
