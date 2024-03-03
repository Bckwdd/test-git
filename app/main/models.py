from django.db import models

# Create your models here.


class Insurance(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    images = models.ImageField(upload_to='insurance')

    def __str__(self):
        return self.title
