# Generated by Django 4.1.4 on 2023-02-11 17:19

from django.db import migrations, models
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=userprofile.models.get_uid),
        ),
    ]
