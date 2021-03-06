# Generated by Django 2.2.6 on 2020-01-09 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('body_configuration', '0001_initial'),
        ('configurations', '0007_auto_20200102_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20, null=True)),
                ('time_of_life', models.TextField(max_length=50, null=True)),
                ('manteinance_cleaning', models.TextField(max_length=50, null=True)),
                ('description', models.TextField(max_length=50, null=True)),
                ('certification', models.TextField(max_length=50, null=True)),
                ('mode_use', models.TextField(max_length=50, null=True)),
                ('status', models.BooleanField(null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('body_area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='body_configuration.BodyPart')),
                ('element_classification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configurations.Element_Classification')),
            ],
        ),
    ]
