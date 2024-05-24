# Generated by Django 5.0.3 on 2024-04-03 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_clubevents'),
    ]

    operations = [
        migrations.CreateModel(
            name='instituitionseventapplctn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('instituitionname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.instituitionevents')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.commonuser')),
            ],
        ),
    ]
