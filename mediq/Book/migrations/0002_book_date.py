# Generated by Django 5.0.4 on 2024-06-29 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date',
            field=models.DateField(default='2023-01-01'),
        ),
    ]
