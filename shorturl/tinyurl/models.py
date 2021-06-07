from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ShortUrlModel(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    hash = models.CharField(max_length=32)
    url = models.TextField()
    click_counter = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('short-link', args=(self.hash, ))
