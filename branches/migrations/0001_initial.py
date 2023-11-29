# Generated by Django 4.2.7 on 2023-11-29 23:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operating_hours', '0001_initial'),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=60)),
                ('zip_code', models.CharField(max_length=5)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=15)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches_company', to='companies.company')),
                ('operating_hours', models.ManyToManyField(related_name='branches', to='operating_hours.operating')),
            ],
        ),
        migrations.AddConstraint(
            model_name='branch',
            constraint=models.UniqueConstraint(fields=('zip_code', 'state', 'city', 'street', 'number'), name='unique_address'),
        ),
    ]
