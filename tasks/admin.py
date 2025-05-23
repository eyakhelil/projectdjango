from django.contrib import admin
from .models import Task, Entity, FieldDefinition, IntegrationLog ,FieldMapping

admin.site.register(Task)
admin.site.register(Entity)
admin.site.register(FieldDefinition)
admin.site.register(IntegrationLog)

@admin.register(FieldMapping)
class FieldMappingAdmin(admin.ModelAdmin):
    list_display = ('django_field', 'lowcode_field', 'created_at')
    ordering = ('-created_at',)
