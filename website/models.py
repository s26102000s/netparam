from django.db import models
from django.db.models.query_utils import select_related_descend
from django.urls import reverse
from django.contrib.auth import get_user_model

from froala_editor.fields import FroalaField


# Create your models here.
User = get_user_model()


class course(models.Model):
    TYPE = (
        ("Industrial Training", "Industrial Training"),
    )
    
    type  = models.CharField(choices=TYPE, max_length=250, default='Industrial Training')
    name = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150, null=True)
    description = FroalaField(theme='dark')
    fees = models.CharField(max_length=10)
    image = models.ImageField(null = True, upload_to= "icons")
    syllabus = models.FileField(null=True, upload_to = "Curriculum" )
    def __str__(self):
        return self.name


class team(models.Model):

    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=250)
    image = models.ImageField(upload_to = "team")


    def __str__(self):
        return self.name

class service(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField()
    bg_image = models.ImageField(upload_to = "service/bg", null=True)
    image = models.ImageField(upload_to = "service")
    subtitle = models.TextField()

    objects = models.Manager()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_detail', args=[str(self.id)])



class product(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to = "product")
    description = models.TextField()

    def __str__(self):
        return self.name

class client(models.Model):
    name = models.CharField(max_length=256, null=True)
    designation = models.CharField(max_length=256, null=True)
    image = models.ImageField(upload_to = "client", null=True)
    review = models.TextField(null=True)
    rating = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', 
                                on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subjact=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    