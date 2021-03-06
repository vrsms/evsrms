# Generated by Django 3.2.5 on 2022-04-26 10:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20220426_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceticket',
            name='service_date',
        ),
        migrations.AddField(
            model_name='serviceticket',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serviceticket',
            name='frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='serviceticket',
            name='item_serviced',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serviceticket',
            name='status',
            field=models.CharField(default='', max_length=30, verbose_name='Operation status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='category',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='plate_number',
            field=models.CharField(default='', max_length=30, verbose_name='Plate number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='status',
            field=models.CharField(default='', max_length=30, verbose_name='Operation status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=30, verbose_name='vehicle_model'),
        ),
    ]
