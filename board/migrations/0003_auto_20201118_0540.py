# Generated by Django 3.1.3 on 2020-11-18 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20201118_0521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_dt',
            new_name='created_dt',
        ),
    ]
