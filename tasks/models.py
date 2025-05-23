from django.db import models
from django.core.exceptions import ValidationError

# Tâche simple (exemple générique)
class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Entité (ex : Client, Commande, etc.)
class Entity(models.Model):
    name = models.CharField(max_length=100)  # ex: "Client", "Commande"

    def __str__(self):
        return self.name
    

# Définition des champs pour chaque entité
class FieldDefinition(models.Model):
    FIELD_TYPE_CHOICES = [
        ('string', 'String'),
        ('number', 'Number'),
        ('date', 'Date'),
    ]

    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="fields")
    field_name = models.CharField(max_length=100)  # ex: "email", "age"
    field_type = models.CharField(max_length=50, choices=FIELD_TYPE_CHOICES)  # contraint à 3 types

    class Meta:
        unique_together = ('entity', 'field_name')  # pas deux fois le même champ dans une entité

    def clean(self):
        if ' ' in self.field_name:
            raise ValidationError("Le nom du champ ne doit pas contenir d'espaces.")

    def __str__(self):
        return f"{self.entity.name} - {self.field_name}"


# Journal des échanges (logs)
class IntegrationLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=True)
    message = models.TextField()