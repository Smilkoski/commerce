# Generated by Django 4.0 on 2021-12-17 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_bid_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='active',
        ),
        migrations.AddField(
            model_name='listing',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
