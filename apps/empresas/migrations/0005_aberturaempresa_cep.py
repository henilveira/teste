# Generated by Django 5.1.1 on 2024-10-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0004_aberturaempresa_empresa_abertura'),
    ]

    operations = [
        migrations.AddField(
            model_name='aberturaempresa',
            name='cep',
            field=models.CharField(default='', max_length=9),
            preserve_default=False,
        ),
    ]
