# Generated by Django 5.0.8 on 2024-08-22 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipoatividade', '0005_tipoatividade_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoatividade',
            name='titulo',
            field=models.CharField(default='', help_text='Informe o titulo do Tipo de Atividade', max_length=70),
        ),
    ]