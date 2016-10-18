from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Car(models.Model):
    slug = models.SlugField(max_length=24,primary_key=True)
    image = models.ImageField(blank=True)
    broken = models.BooleanField(default=False)

    def __unicode__(self):
        return self.slug