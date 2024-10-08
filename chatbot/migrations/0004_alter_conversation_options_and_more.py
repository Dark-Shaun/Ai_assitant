# Generated by Django 5.1.1 on 2024-09-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_alter_conversation_context'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation',
            options={'ordering': ['-timestamp']},
        ),
        migrations.RenameField(
            model_name='conversation',
            old_name='bot_response',
            new_name='assistant_response',
        ),
        migrations.AlterField(
            model_name='conversation',
            name='context',
            field=models.TextField(blank=True),
        ),
    ]
