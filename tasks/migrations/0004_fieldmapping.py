# Generated by Django 5.2.1 on 2025-05-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_fielddefinition_field_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('django_field', models.CharField(max_length=100)),
                ('lowcode_field', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
