from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from ocr_app.forms import OCRForm

from django.views.generic import DetailView
from ocr_app.models import Reader

global dic
dic={'data': 'data'}

class OCR_Root(TemplateView):
#view for OCR home template
    form = OCRForm
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):

        form = OCRForm(request.POST, request.FILES)
        print(request.POST)

        if form.is_valid():
            obj,data = form.save()
            dic['data']=data
            return HttpResponseRedirect(reverse_lazy('pan_display', kwargs={'pk': obj.id}))


        if 'run_script' in request.POST:

            # import function to run
            from ocr_app.clear_media import test

            # call function
            test() 

            # return user to required page
           


        context = self.get_context_data(form=form)
        return self.render_to_response(context)

         

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    

class PanDetails(DetailView):
#view for Pan card display template
    model = Reader
    template_name = 'pan_display.html'
    context_object_name = 'ocr'

    def get_context_data(self, **kwargs):
        context = super(PanDetails, self).get_context_data(**kwargs)
        context.update({'content': dic['data']})
        return context

