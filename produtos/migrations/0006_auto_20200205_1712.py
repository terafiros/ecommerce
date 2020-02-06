# Generated by Django 3.0.3 on 2020-02-05 20:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_auto_20200205_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='desconto',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(limit_value=0)]),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(limit_value=0)]),
        ),
    ]
