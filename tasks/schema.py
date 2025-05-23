import graphene
from graphene_django.types import DjangoObjectType
from .models import Entity, FieldDefinition, IntegrationLog

# --- Types GraphQL ---
class EntityType(DjangoObjectType):
    class Meta:
        model = Entity

class FieldType(DjangoObjectType):
    class Meta:
        model = FieldDefinition

class LogType(DjangoObjectType):
    class Meta:
        model = IntegrationLog

# --- Mutation pour créer une Entity ---
class CreateEntity(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    entity = graphene.Field(EntityType)

    def mutate(self, info, name):
        entity = Entity.objects.create(name=name)
        return CreateEntity(entity=entity)

# --- Requêtes disponibles ---
class Query(graphene.ObjectType):
    entities = graphene.List(EntityType)
    fields = graphene.List(FieldType)
    logs = graphene.List(LogType)

    def resolve_entities(root, info):
        return Entity.objects.all()

    def resolve_fields(root, info):
        return FieldDefinition.objects.all()

    def resolve_logs(root, info):
        return IntegrationLog.objects.all()

# --- Mutations disponibles ---
class Mutation(graphene.ObjectType):
    create_entity = CreateEntity.Field()

# --- Schéma final ---
schema = graphene.Schema(query=Query, mutation=Mutation)
