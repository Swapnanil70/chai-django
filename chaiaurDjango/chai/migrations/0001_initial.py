# Generated by Django 5.1.2 on 2024-10-24 17:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiVariety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='chais/')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('ML', 'MASALA'), ('GR', 'GINGER'), ('KL', 'KESAR'), ('PL', 'PLAIN'), ('EL', 'ELAICHI')], max_length=2)),
            ],
        ),
    ]
