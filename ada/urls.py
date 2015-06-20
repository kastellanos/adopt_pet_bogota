__author__ = 'Andres'

from django.conf.urls import url
from django.conf import settings
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^adoptions/$', views.PetAdoptionView.as_view(), name='pet-adoption'),
    url(r'^contact/$', TemplateView.as_view(template_name="ada/contacto.html"), name='contact-info'),
    url(r'^esterilizar/$', TemplateView.as_view(template_name="ada/esterilizar.html"), name='esterilizar'),
    url(r'^process/$', views.ProcessInfoView.as_view(), name='process-adoption'),
    url(r'^(?P<pk>[0-9]+)/$',views.PetInfoView.as_view(),name='pet-info'),
    url(r'^tenencia/$', TemplateView.as_view(template_name="ada/tenencias-responsables.html"), name='tenencia'),

]

