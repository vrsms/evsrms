# Generated by Django 3.2.5 on 2022-04-26 10:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20220426_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceticket',
            name='date',
        ),
        migrations.RemoveField(
            model_name='serviceticket',
            name='frequency',
        ),
        migrations.RemoveField(
            model_name='serviceticket',
            name='item_serviced',
        ),
        migrations.RemoveField(
            model_name='serviceticket',
            name='status',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='category',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='plate_number',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='status',
        ),
        migrations.AddField(
            model_name='serviceticket',
            name='service_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ServiceTicket Date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=20, verbose_name='vehicle_model'),
        ),
    ]
