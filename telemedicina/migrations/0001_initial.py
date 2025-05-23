# Generated by Django 5.2 on 2025-04-23 23:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultas', '0004_consulta_unidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telemedicina',
            fields=[
                ('consulta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='consultas.consulta')),
                ('link_sala', models.URLField(blank=True, null=True)),
                ('registro_video', models.URLField(blank=True, null=True)),
            ],
            bases=('consultas.consulta',),
        ),
    ]
