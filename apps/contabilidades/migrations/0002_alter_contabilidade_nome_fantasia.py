# Generated by Django 5.1.1 on 2024-09-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contabilidade',
            name='nome_fantasia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
