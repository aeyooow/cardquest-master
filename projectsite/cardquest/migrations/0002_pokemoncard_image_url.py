# Generated by Django 5.0 on 2023-12-17 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardquest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemoncard',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
