# forms.py 
from django import forms 
from .models import Reader
from django.core.files import File
from PIL import Image
from OCR import handler
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#this form is used to extract image data from the end-user, The pan details are extracted here with the use of the handler function
class OCRForm(forms.ModelForm): 
  
    class Meta: 
        model = Reader 
        fields = ['pan_image']

    def save(self):

        photo = super(OCRForm, self).save()

        image = Image.open(photo.pan_image)
        loc=str(photo.pan_image.path)

        image.save(photo.pan_image.path)
        name,DOB,pan=handler(loc[1:])

        return photo,name,DOB,pan