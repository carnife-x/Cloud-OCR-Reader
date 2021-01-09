#from django.contrib.auth.models import User
#settings.configure()
#User.objects.create_superuser('steve', 'stevejefferson.g@gmail.com', '123pass')

from django.contrib import admin

from ocr_app.models import Reader

admin.site.register(Reader)