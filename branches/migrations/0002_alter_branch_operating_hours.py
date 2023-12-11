# Generated by Django 4.0 on 2023-12-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operating_hours', '0001_initial'),
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='operating_hours',
            field=models.ManyToManyField(related_name='branches', to='operating_hours.Operating'),
        ),
    ]