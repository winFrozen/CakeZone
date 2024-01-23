from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Aboutus(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Aboutus/img')

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    bio = models.TextField()
    img = models.ImageField(upload_to='Menu/img')
    slug = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("menu_detail_view", args=[self.slug])

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Team/img')
    slug = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("team_detail_view", args=[self.slug])

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    comment = models.TextField()
    img = models.ImageField(upload_to='Testimonial/img')
    slug = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("testiDetail", args=[self.slug])

    def __str__(self):
        return self.name

class Menu2(models.Model):
        name = models.CharField(max_length=100)
        price = models.IntegerField()
        bio = models.TextField()
        img = models.ImageField(upload_to='Menu2/img')
        slug = models.CharField(max_length=100)

        def get_absolute_url(self):
            return reverse("menu2_detail_view", args=[self.slug])

        def __str__(self):
            return self.name


class Menu3(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    bio = models.TextField()
    img = models.ImageField(upload_to='Menu3/img')
    slug = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("menu3_detail_view", args=[self.slug])

    def __str__(self):
        return self.name

class veb(models.Model):
    name =models.CharField(max_length=300)