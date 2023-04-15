from django.contrib import admin
from . import models


class ModelAdmin(admin.ModelAdmin):
    list_display = ('group', 'order', 'name', 'slug', 'parent', )


admin.site.register(models.MenuGroup)
admin.site.register(models.Menu, ModelAdmin)
