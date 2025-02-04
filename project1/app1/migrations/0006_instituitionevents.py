# Generated by Django 5.0.3 on 2024-04-02 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_clubs'),
    ]

    operations = [
        migrations.CreateModel(
            name='instituitionevents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('event_date', models.DateField(max_length=200)),
                ('instituitionname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.instituitions')),
            ],
        ),
    ]
