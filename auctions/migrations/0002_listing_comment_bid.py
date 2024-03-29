# Generated by Django 4.0 on 2021-12-13 23:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(blank='', max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(default='', upload_to='listings_images')),
                ('category', models.CharField(choices=[('FA', 'Fashion'), ('SP', 'Sport'), ('TO', 'Toys'), ('EL', 'Electronic'), ('HO', 'Home')], default='FA', max_length=15)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='auctions.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('listing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_comment', to='auctions.listing')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to='auctions.user')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('listing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_user', to='auctions.listing')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid_user', to='auctions.user')),
            ],
        ),
    ]
