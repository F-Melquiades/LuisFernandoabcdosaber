# Generated by Django 5.0.8 on 2024-08-22 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titulo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipoatividade',
            name='descricao',
        ),
        migrations.AlterField(
            model_name='tipoatividade',
            name='titulo',
            field=models.CharField(help_text='Informe a descrição do Tipo de Atividade', max_length=70),
        ),
    ]
