from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.TextField()
    description = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
