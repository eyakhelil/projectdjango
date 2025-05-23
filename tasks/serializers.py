from rest_framework import serializers
from .models import Task, Entity, FieldDefinition, IntegrationLog

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# --- Serializer pour Entity ---
class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'

# --- Serializer pour FieldDefinition avec validation personnalisée ---
class FieldDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldDefinition
        fields = '__all__'

def validate_field_type(self, value):
    allowed = ['string', 'number', 'boolean']
    if value not in allowed:
        raise serializers.ValidationError("Type non supporté. Utilise: string, number ou boolean.")
    return value


# --- Serializer pour les logs d’intégration ---
class IntegrationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationLog
        fields = '__all__'
