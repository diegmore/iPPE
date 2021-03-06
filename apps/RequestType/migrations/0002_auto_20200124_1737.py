# Generated by Django 2.2 on 2020-01-24 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestType', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request_type',
            name='element_type_id',
        ),
        migrations.AlterField(
            model_name='request_type',
            name='Status',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='request_type',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='request_type',
            name='detail',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='request_type',
            name='name',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
