# Generated by Django 4.2.3 on 2023-07-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrap_request',
            name='readed',
            field=models.BooleanField(default=False),
        ),
    ]
