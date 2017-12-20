from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Effect(models.Model):
	name = models.CharField(max_length=20)
	consequences = JSONField()
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Effects"

class Skill(models.Model):
	name = models.CharField(max_length=20)
	duration = models.IntegerField()
	effects = models.ManyToManyField(Effect)
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Skills"

class Breed(models.Model):
	name = models.CharField(max_length=20)
	habitat = models.CharField(max_length=20, default='Forest')
	mean_height = models.FloatField()
	passive_skill = models.ManyToManyField(Skill)
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Breeds"

class Clothes_family(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Clothes_Families"

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

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Clothes"

class Weapons_family(models.Model):
	name = models.CharField(max_length=20)
	range = models.IntegerField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Weapons_families"

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
	damage = models.IntegerField(default=0)
	extras = JSONField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Weapons"

class Class(models.Model):
	name = models.CharField(max_length=20)
	weapons = models.ManyToManyField(Weapons_family)
	skills = models.ManyToManyField(Skill)
	clothes = models.ManyToManyField(Clothes_family)
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Classes"

class Object(models.Model):
	name = models.CharField(max_length=25)
	description = models.CharField(max_length=140)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Objects"

class Char(models.Model):
	name = models.CharField(max_length=25)
	breed = models.OneToOneField(
		Breed,
		on_delete=models.CASCADE
	)
	klass = models.OneToOneField(
		Class,
		on_delete=models.CASCADE
	)
	age = models.IntegerField()
	sex = models.CharField(max_length=12)
	clothes = models.ManyToManyField(Clothes)
	weapons = models.ManyToManyField(Weapon)
	bag = models.ManyToManyField(Object)
	story = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class PlayerUser(AbstractBaseUser):
    username = models.CharField(max_length=25, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    master = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

    @property
    def is_admin(self):
    	return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
