# Generated by Django 3.0.6 on 2020-05-20 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20200520_1135'),
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='cities.City'),
            preserve_default=False,
        ),
    ]
