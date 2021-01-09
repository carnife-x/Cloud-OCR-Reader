# forms.py 
from django import forms 
from .models import Reader
from django.core.files import File
from PIL import Image
from OCR import handler

#this form is used to extract image data from the end-user, The pan details are extracted here with the use of the handler function
class OCRForm(forms.ModelForm): 
  
    class Meta: 
        model = Reader 
        fields = ['pan_image']

    def save(self):
        photo = super(OCRForm, self).save()

        image = Image.open(photo.pan_image)
        loc=str(photo.pan_image.url)

        image.save(photo.pan_image.path)
        data=handler(loc[1:])

        return photo,data