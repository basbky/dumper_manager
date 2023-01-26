from django.contrib import admin

from .models import Dumper, Model


class ModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'load_capacity',
    )
    search_fields = ('name',)
    list_filter = ('load_capacity',)


class DumperAdmin(admin.ModelAdmin):
    list_display = (
        'tail_number',
        'model',
        'load_weight',
    )
    search_fields = ('tail_number',)
    list_filter = ('load_weight',)


admin.site.register(Model, ModelAdmin)
admin.site.register(Dumper, DumperAdmin)
