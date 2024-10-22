# Generated by Django 5.1.2 on 2024-10-12 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startit_app', '0004_quest_chislo_alter_strashno_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='quest',
            name='chislo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startit_app.chislo', verbose_name='Выберите количество'),
        ),
    ]