from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TaskViewSet,
    EntityViewSet,
    FieldDefinitionViewSet,
    IntegrationLogViewSet,
    submit_data
)

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'entities', EntityViewSet)
router.register(r'fields', FieldDefinitionViewSet)
router.register(r'logs', IntegrationLogViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/submit/', submit_data),  # endpoint spécial
]
