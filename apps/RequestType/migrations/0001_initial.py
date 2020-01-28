


from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configurations', '0007_auto_20200102_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.TextField(max_length=50)),
                ('detail', models.TextField(max_length=50)),
                ('Status', models.TextField(max_length=50)),
                ('element_type_id', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='configurations.Element_Type')),
            ],
        ),
    ]
