import json

# Fonction pour générer un prompt structuré
def generate_mapping_prompt(django_fields, lowcode_fields):
    return {
        "instruction": "Fais le mappage entre les champs Django et ceux de la plateforme low-code.",
        "django_fields": django_fields,
        "lowcode_fields": lowcode_fields,
        "format": {
            "mapping": {
                "django_field": "lowcode_field"
            }
        }
    }

# Simulation de la fonction GPT : réponse fixe
def get_mapping_suggestion(prompt_json):
    print("Simulation activée : GPT n'est pas utilisé.")

    # Exemple de correspondance simple
    simulated_response = {
        "mapping": [
            {"django_field": "name", "lowcode_field": "full_name"},
            {"django_field": "email", "lowcode_field": "email_address"},
            {"django_field": "created_at", "lowcode_field": "date_created"},
        ]
    }
    return simulated_response
