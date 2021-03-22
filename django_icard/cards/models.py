from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    profile_image = models.ImageField(max_length=255, upload_to='image')
    created_on = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField(max_length=30)
    contact_email = models.EmailField(max_length=255)
    contact_phone = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='creator')
    favorited_users = models.ManyToManyField(User)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.ordering
