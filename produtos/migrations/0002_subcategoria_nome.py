# Generated by Django 3.0.3 on 2020-02-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategoria',
            name='nome',
            field=models.CharField(default='', max_length=200),
        ),
    ]
