# Generated by Django 5.0.3 on 2024-05-18 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=200)),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product')),
                ('productname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_by_productname', to='app1.product')),
                ('shopname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_by_shopname', to='app1.product')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.commonuser')),
            ],
        ),
    ]
