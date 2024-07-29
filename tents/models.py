from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
# Create your models here.


class Tent(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='tent_photos/')
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def get_absolute_url(self):
        return reverse('tent_detail', args=[str(self.id)])


###########################################################################



