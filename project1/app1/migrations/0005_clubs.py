# Generated by Django 5.0.3 on 2024-03-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_shops'),
    ]

    operations = [
        migrations.CreateModel(
            name='clubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clubname', models.CharField(max_length=200)),
                ('managername', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('clubid', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='clb')),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
