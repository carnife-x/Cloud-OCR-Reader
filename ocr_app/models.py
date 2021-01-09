from django.db import models
import os
# Model is created to save the location of images

class Reader(models.Model):
    pan_image = models.ImageField(upload_to='images/')

