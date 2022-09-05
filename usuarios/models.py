from contextlib import nullcontext
from django.db import models


class User_profile(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='profile_image/', blank=True, null=True)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username + ' - profile'