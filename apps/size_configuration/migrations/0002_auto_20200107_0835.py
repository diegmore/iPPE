# Generated by Django 2.2.6 on 2020-01-07 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('size_configuration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
