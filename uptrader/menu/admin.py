from django.contrib import admin
from . import models


class ModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'parent', 'group', 'first_level')
    filter_horizontal = ['childes']


admin.site.register(models.MenuGroup)
admin.site.register(models.Menu, ModelAdmin)
