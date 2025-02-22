# Generated by Django 5.1.1 on 2024-10-19 02:44

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societario', '0004_nomeprocessos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Processos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status_processo', models.BooleanField(default=False)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='societario.aberturaempresa')),
                ('etapa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='societario.etapas')),
                ('nome_processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='societario.nomeprocessos')),
            ],
        ),
    ]
