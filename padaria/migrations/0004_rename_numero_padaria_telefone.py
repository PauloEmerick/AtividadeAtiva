# Generated by Django 4.2.7 on 2023-11-25 14:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("padaria", "0003_rename_horario_padaria_dia"),
    ]

    operations = [
        migrations.RenameField(
            model_name="padaria",
            old_name="numero",
            new_name="telefone",
        ),
    ]
