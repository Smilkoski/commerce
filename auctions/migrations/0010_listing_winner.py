# Generated by Django 4.0 on 2021-12-17 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_bid_active_listing_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='winner',
            field=models.IntegerField(default=-1),
        ),
    ]
