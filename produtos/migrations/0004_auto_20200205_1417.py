# Generated by Django 3.0.3 on 2020-02-05 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_categoria_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descricao',
            field=models.CharField(default='Venha conferir nossos produtos', max_length=200),
        ),
    ]