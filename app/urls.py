from distutils.command.upload import upload
from .views import *
import imp
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    url(r'^HomePageView',HomePageView.as_view(),name="HomePageView"),
    url(r'^dataset/', dataset, name='dataset'),
    url(r'^plot_and_commute/', plot_and_commute.as_view(), name='plot_and_commute'),
    url(r'^save_data/',save_data,name='save_data'),
    url(r'^plot_data/',plot_data,name='plot_data'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)