# Generated by Django 5.0.8 on 2024-08-22 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAtividade',
            fields=[
                ('codigo', models.AutoField(help_text='Código do Tipo de atividade', primary_key=True, serialize=False)),
                ('descricao', models.CharField(help_text='Informe a descrição do Tipo de Atividade', max_length=70)),
                ('titulo', models.CharField(default='', help_text='Informe o titulo do Tipo de Atividade', max_length=70)),
            ],
        ),
    ]