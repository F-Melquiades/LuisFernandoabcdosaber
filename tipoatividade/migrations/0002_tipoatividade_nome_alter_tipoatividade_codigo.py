# Generated by Django 5.0.8 on 2024-08-22 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipoatividade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoatividade',
            name='nome',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tipoatividade',
            name='codigo',
            field=models.AutoField(help_text='Código do Tipo de atividade', primary_key=True, serialize=False),
        ),
    ]
