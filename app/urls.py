from django.urls import path,re_path
from . import views
from . import contact

urlpatterns = [
    #path('<int:year>/<str:month>/',views.index,name='index'), #path converters (str,int,slug,UUID,path)
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/',views.index,name='index'),
    path('',views.index,name='index'),
    path('contact/',contact.contact,name='contact'),
    path('event/',views.event,name='event'),
    path('all_events/',views.all_events,name='all_events'),
    ]
