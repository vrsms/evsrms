# Generated by Django 3.2.5 on 2022-05-25 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kyc', '0001_initial'),
        ('suggestions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kyc.vehicle'),
        ),
    ]