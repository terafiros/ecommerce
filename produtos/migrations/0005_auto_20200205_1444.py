# Generated by Django 3.0.3 on 2020-02-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_auto_20200205_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='desconto',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='produtos',
            name='promocao',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
