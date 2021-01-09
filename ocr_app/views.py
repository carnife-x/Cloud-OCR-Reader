from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from ocr_app.forms import OCRForm

from django.views.generic import DetailView
from ocr_app.models import Reader

global dic
dic={'name': 'name', 'DOB': 'DOB', 'pan':'pan'}

class OCR_Root(TemplateView):
#view for OCR home template
    form = OCRForm
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):

        form = OCRForm(request.POST, request.FILES)

        if form.is_valid():
            obj,name,DOB,pan = form.save()
            dic['name']=name
            dic['DOB']=DOB
            dic['pan']=pan
            return HttpResponseRedirect(reverse_lazy('pan_display', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    

class PanDetails(DetailView):
#view for Pan card display template
    var1 = dic['name']
    model = Reader
    template_name = 'pan_display.html'
    context_object_name = 'ocr'

    def get_context_data(self, **kwargs):
        context = super(PanDetails, self).get_context_data(**kwargs)
        context.update({'nam': dic['name'], 'DO': dic['DOB'], 'pa': dic['pan']})
        return context