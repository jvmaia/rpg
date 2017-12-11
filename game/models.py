from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

class Effect(models.Model):
	name = models.CharField(max_length=20)
	consequences = JSONField()
	description = models.CharField(max_length=100)

class Skill(models.Model):
	name = models.CharField(max_length=20)
	duration = models.IntegerField()
	effects = models.ManyToManyField(Effect)
	description = models.CharField(max_length=100)

class Breed(models.Model):
	name = models.CharField(max_length=20)
	mean_height = models.FloatField()
	passive_skill = models.ManyToManyField(Skill)
	description = models.CharField(max_length=200)

class Clothes_family(models.Model):
	name = models.CharField(max_length=20)

class Clothes(models.Model):
	name = models.CharField(max_length=20)
	family = models.ForeignKey(
		'Clothes_family',
		on_delete=models.SET_NULL,
		blank=True,
		null=True
	)
	description = models.CharField(max_length=100)
	weight = models.IntegerField()
	extras = JSONField()

class Weapons_family(models.Model):
	name = models.CharField(max_length=20)
	range = models.IntegerField()

class Weapon(models.Model):
	choices_hand = (
		('1', 'One-hand'),
		('2', 'Two-hands')
	)
	name = models.CharField(max_length=20)
	family = models.ForeignKey(
		'Weapons_family',
		on_delete=models.SET_NULL,
		blank=True,
		null=True
	)
	hands = models.CharField(
		choices=choices_hand,
		max_length=1
	)
	extras = JSONField()

class Class(models.Model):
	name = models.CharField(max_length=20)
	weapons = models.ManyToManyField(Weapons_family)
	skills = models.ManyToManyField(Skill)
	clothes = models.ManyToManyField(Clothes_family)
	description = models.CharField(max_length=200)
