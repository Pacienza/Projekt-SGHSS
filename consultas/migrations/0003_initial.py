# Generated by Django 5.2 on 2025-04-22 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultas', '0002_initial'),
        ('profissionais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='profissionais.profissionalsaude'),
        ),
    ]
