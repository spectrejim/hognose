# Generated by Django 3.0.3 on 2020-05-20 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scenario',
            name='front',
        ),
        migrations.RemoveField(
            model_name='scenario',
            name='location',
        ),
        migrations.RemoveField(
            model_name='scenario',
            name='maps',
        ),
        migrations.RemoveField(
            model_name='scenario',
            name='sides',
        ),
        migrations.RemoveField(
            model_name='scenario',
            name='source',
        ),
        migrations.RemoveField(
            model_name='scenario',
            name='time',
        ),
    ]
