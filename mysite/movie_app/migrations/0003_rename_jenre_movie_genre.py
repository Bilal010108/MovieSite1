# Generated by Django 5.1.3 on 2024-11-26 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_alter_actor_actor_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='jenre',
            new_name='genre',
        ),
    ]