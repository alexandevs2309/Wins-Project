# Generated by Django 5.1.3 on 2024-12-15 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticacion', '0008_rename_profile_picture_customuser_profilepicture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profilePicture',
        ),
    ]
