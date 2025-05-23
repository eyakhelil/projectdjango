from celery import shared_task
from .models import FieldMapping
from .ai_utils import generate_mapping_prompt, get_mapping_suggestion

@shared_task
def sync_data_with_lowcode():
    print(" Synchronisation des données avec la plateforme low-code...")
    return "Synchronisation OK"

@shared_task
def generate_mapping_task():
    print("Simulation activée : GPT n'est pas utilisé.")
    
    # Simuler un résultat de mapping
    simulated_result = {
        "mapping": [
            {"django_field": "name", "lowcode_field": "full_name"},
            {"django_field": "email", "lowcode_field": "email_address"},
            {"django_field": "created_at", "lowcode_field": "date_created"}
        ]
    }

    # Enregistrer chaque correspondance dans la base de données
    for item in simulated_result["mapping"]:
        FieldMapping.objects.create(
            django_field=item["django_field"],
            lowcode_field=item["lowcode_field"]
        )

    # Afficher dans les logs (console)
    print("Mapping suggéré par IA :", simulated_result)

    return simulated_result
