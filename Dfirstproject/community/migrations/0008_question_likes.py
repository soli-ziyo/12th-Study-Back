# Generated by Django 4.2.11 on 2024-04-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(to='community.like'),
        ),
    ]
