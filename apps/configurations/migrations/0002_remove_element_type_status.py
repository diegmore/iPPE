# Generated by Django 2.2.6 on 2019-12-18 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element_type',
            name='status',
        ),
    ]
