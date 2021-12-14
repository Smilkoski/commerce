from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


CATEGORIES = (
    ('Fashion', 'FA'),
    ('Sport', 'SP'),
    ('Toys', 'TO'),
    ('Electronic', 'EL'),
    ('Home', 'HO'),
)


class Listing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200, blank='')
    price = models.IntegerField()
    image = models.ImageField(default='default.jpg', upload_to='listings_images')
    category = models.CharField(max_length=15, choices=CATEGORIES, default='FA')
    date_created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Bid(models.Model):
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing_user')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bid_user')
    price = models.IntegerField()


class Comment(models.Model):
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing_comment')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.CharField(max_length=100)


class Watchlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_watchlist')
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='user_listings')
