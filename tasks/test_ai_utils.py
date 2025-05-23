from ai_utils import generate_mapping_prompt, get_mapping_suggestion

django_fields = ["name", "email", "created_at"]
lowcode_fields = ["full_name", "email_address", "date_created"]

prompt = generate_mapping_prompt(django_fields, lowcode_fields)
print("Prompt JSON :")
print(prompt)

print("\n Résultat AI :")
response = get_mapping_suggestion(prompt)
print(response)
