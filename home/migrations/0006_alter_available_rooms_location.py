# Generated by Django 4.1.4 on 2022-12-28 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_available_rooms_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='available_rooms',
            name='location',
            field=models.JSONField(default=list),
        ),
    ]
