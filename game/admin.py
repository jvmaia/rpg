from django.contrib import admin
from .models import (Effect, Skill,
    Breed, Clothes_family, Clothes,
    Weapons_family, Weapon, Class, Char)

admin.site.register(Effect)
admin.site.register(Weapons_family)
admin.site.register(Clothes_family)

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration']
admin.site.register(Skill, SkillAdmin)

class BreedAdmin(admin.ModelAdmin):
    list_display = ['name', 'habitat']
admin.site.register(Breed, BreedAdmin)

class ClothesAdmin(admin.ModelAdmin):
    list_display = ['name', 'weight', 'family']
admin.site.register(Clothes, ClothesAdmin)

class WeaponAdmin(admin.ModelAdmin):
    list_display = ['name', 'hands', 'damage', 'family']
admin.site.register(Weapon, WeaponAdmin)

class ClassAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Class, ClassAdmin)

class CharAdmin(admin.ModelAdmin):
    fields = ['name', 'age',
    'sex', 'breed', 'klass']
    list_display = ['name', 'breed', 'klass', 'level']
admin.site.register(Char, CharAdmin)
