from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Card(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.ordering
