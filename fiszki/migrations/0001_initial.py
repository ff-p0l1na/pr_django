# Generated by Django 4.1.7 on 2023-03-19 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fiszka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('przod', models.CharField(max_length=100, verbose_name='Przód karty')),
                ('tyl', models.CharField(max_length=100, verbose_name='Tył karty')),
                ('mnemo', models.CharField(max_length=300, verbose_name='Zdanie ułatwiające zapamiętanie')),
            ],
        ),
    ]
