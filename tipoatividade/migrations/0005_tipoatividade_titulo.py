# Generated by Django 5.0.8 on 2024-08-22 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipoatividade', '0004_merge_20240822_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoatividade',
            name='titulo',
            field=models.CharField(help_text='Informe o titulo do Tipo de Atividade', max_length=70, null=True),
        ),
    ]
