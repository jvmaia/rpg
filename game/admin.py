from django.contrib import admin
from .models import (Effect, Skill,
    Breed, Clothes_family, Clothes,
    Weapons_family, Weapon, Class, Char)


admin.site.register(Effect)
admin.site.register(Skill)
admin.site.register(Breed)
admin.site.register(Clothes_family)
admin.site.register(Clothes)
admin.site.register(Weapons_family)
admin.site.register(Weapon)
admin.site.register(Class)

class CharAdmin(admin.ModelAdmin):
    fields = ['name', 'age',
    'sex', 'breed', 'klass']
    list_display = ['name', 'breed', 'klass', 'level']

admin.site.register(Char, CharAdmin)
