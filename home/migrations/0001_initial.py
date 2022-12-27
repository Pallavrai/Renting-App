# Generated by Django 4.1.4 on 2022-12-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='available_rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.IntegerField()),
                ('title', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=255)),
                ('visits', models.IntegerField()),
                ('current_members', models.CharField(max_length=25)),
                ('rooms', models.IntegerField()),
                ('Price', models.IntegerField()),
            ],
        ),
    ]