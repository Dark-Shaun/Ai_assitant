# Generated by Django 5.1.1 on 2024-09-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_alter_conversation_context'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='context',
            field=models.TextField(default=''),
        ),
    ]
