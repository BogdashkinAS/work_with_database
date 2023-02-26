from django.db import models
from django.urls import reverse
from django.shortcuts import render, reverse
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length= 100)
    price = models.IntegerField()
    image = models.CharField(max_length= 250)
    release_date = models.DateField(max_length= 50)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length= 100, editable=False, unique=True)

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
