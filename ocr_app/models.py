from django.db import models

# Model is created to save the location of images

class Reader(models.Model):
    pan_image = models.ImageField(upload_to='images/')

