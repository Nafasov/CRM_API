# Generated by Django 5.0.6 on 2024-05-30 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_group_add_group_alter_worker_added_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GroupComment',
        ),
    ]