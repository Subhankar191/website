# Generated by Django 5.1.2 on 2024-10-20 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_info_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='mobile_number',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='user_id',
            new_name='username',
        ),
    ]
