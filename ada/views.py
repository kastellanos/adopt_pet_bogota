
from .models import Pet,Article
from django.views import  generic


class IndexView(generic.ListView):
    template_name= 'ada/index.html'
    context_object_name = 'lista'
    def get_queryset(self):
        return Pet.objects.all()

class PetAdoptionView(generic.ListView):
    template_name= 'ada/pet-adoption.html'
    context_object_name = 'lista'
    def get_queryset(self):
        return Article.objects.all()


class PetInfoView(generic.DetailView):
    model = Pet
    template_name = 'ada/pet-info.html'

class ProcessInfoView(generic.ListView):
    template_name = 'ada/adoption_process.html'
    context_object_name = 'lista'
    def get_queryset(self):
        return Article.objects.all().filter(theme="proceso")

class AyudaView(generic.ListView):
    template_name = 'ada/ayuda.html'
    context_object_name = 'lista'
    def get_queryset(self):
        return Article.objects.all().filter(theme="ayuda")

