from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.postgres.fields import JSONField, ArrayField
from django.template.defaultfilters import slugify
from datetime import date


class Map(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='maps/')

    def image_tag(self):
        if len(self.image) > 0:
            return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))
    image_tag.short_description = 'Map'

    def link(self):
        return mark_safe('/media/%s' % (self.image))

    def __str__(self):
        return self.name


class Effect(models.Model):
    name = models.CharField(max_length=20)
    consequences = JSONField(default={None: None})
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Effects"


class Skill(models.Model):
    name = models.CharField(max_length=20)
    min_level = models.PositiveIntegerField()
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
    extras = JSONField(default={None: None})

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
        Weapons_family,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    hands = models.CharField(
        choices=choices_hand,
        max_length=1
    )
    damage = models.IntegerField(default=0)
    extras = JSONField(default={None: None})
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Weapon, self).save(*args, **kwargs)

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
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Object, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Objects"


class Char(models.Model):
    name = models.CharField(max_length=25)
    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE
    )
    klass = models.ForeignKey(
        Class,
        on_delete=models.CASCADE
    )
    life = models.PositiveIntegerField()
    actual_life = models.PositiveIntegerField()
    age = models.IntegerField()
    level = models.IntegerField(default=1)
    sex = models.CharField(max_length=12)
    clothes = models.ManyToManyField(Clothes)
    weapons = models.ManyToManyField(Weapon)
    bag = models.ManyToManyField(Object)
    slug = models.SlugField()

    def getAvailableSkills(self):
        all_skills = []
        all_skills += list(self.breed.passive_skill.values())
        all_skills += list(self.klass.skills.values())

        skills = list(
            filter(lambda x: x['min_level'] <= self.level, all_skills))

        return skills

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Char, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Game(models.Model):
    date = models.DateField(default=date.today)
    rounds = models.PositiveIntegerField()

    def __str__(self):
        return self.name
