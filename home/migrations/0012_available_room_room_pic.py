# Generated by Django 4.1.4 on 2023-02-10 16:48

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_available_room_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='available_room',
            name='room_pic',
            field=models.ImageField(null=True, upload_to=home.models.get_uid),
        ),
    ]
