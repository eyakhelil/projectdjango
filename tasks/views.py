from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .permissions import HasAPIKey

from .models import Task, Entity, FieldDefinition, IntegrationLog
from .serializers import (
    TaskSerializer,
    EntitySerializer,
    FieldDefinitionSerializer,
    IntegrationLogSerializer
)

# --- Vue pour le modèle Task ---
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# --- Vue pour Entity ---
class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = [HasAPIKey]

# --- Vue pour FieldDefinition ---
class FieldDefinitionViewSet(viewsets.ModelViewSet):
    queryset = FieldDefinition.objects.all()
    serializer_class = FieldDefinitionSerializer
    permission_classes = [HasAPIKey]

# --- Vue pour IntegrationLog ---
class IntegrationLogViewSet(viewsets.ModelViewSet):
    queryset = IntegrationLog.objects.all()
    serializer_class = IntegrationLogSerializer
    permission_classes = [HasAPIKey]

# --- Endpoint spécial pour soumettre des données depuis un outil low-code ---
@api_view(['POST'])
def submit_data(request):
    # On logue simplement les données reçues dans IntegrationLog
    log = IntegrationLog.objects.create(
        message=str(request.data),
        success=True  # tu peux ajouter des vérifs ici plus tard
    )
    return Response({
        "message": "Données reçues avec succès.",
        "log_id": log.id
    }, status=status.HTTP_200_OK)
