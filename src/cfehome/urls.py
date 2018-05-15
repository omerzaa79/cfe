from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from restaurants import views


urlpatterns = [
    
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.TemplateView.as_view(template_name='home.html')),
    
    url(r'^restaurants/$', views.RestaurantListView.as_view()),
    
    url(r'^restaurants/create/$', views.RestaurantCreateView.as_view()),
    
    url(r'^restaurants/(?P<slug>[\w-]+)/$', views.RestaurantDetailView.as_view()),
    
    url(r'^about/$', views.TemplateView.as_view(template_name='about.html')),
    
    url(r'^contact/$', views.TemplateView.as_view(template_name='contact.html')),

]