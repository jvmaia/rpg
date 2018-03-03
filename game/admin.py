from django.contrib import admin
from .models import (Effect, Skill,
    Breed, Clothes_family, Clothes,
    Weapons_family, Weapon, Class,
    Char, Map, Object)

admin.site.register(Effect)
admin.site.register(Weapons_family)
admin.site.register(Clothes_family)
admin.site.register(Object)

class MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    fields = ('name', 'image', 'image_tag')
    readonly_fields = ('image_tag',)
admin.site.register(Map, MapAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'min_level']
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
    fieldsets = [
        ('Character', {'fields': ['name', 'life', 'actual_life', 'age',
            'sex', 'breed', 'klass']}),
        ('Equipments', {'fields': ['bag', 'weapons']})
    ]
    list_display = ['name', 'breed', 'klass', 'level']
admin.site.register(Char, CharAdmin)
