# Generated by Django 2.2.6 on 2019-12-19 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0003_element_classification_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='element_classification',
            name='element_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.Element_Type'),
        ),
    ]
