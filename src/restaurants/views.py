from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import RestaurantLocationCreateForm
from .models import RestaurantLocation


class RestaurantListView(ListView):
    queryset = RestaurantLocation.objects.all()


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()


class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/form.html'
    success_url = "/restaurants/"


# class RestaurantListView(ListView):
#     queryset = RestaurantLocation.objects.all()
    
# def get_queryset(self):
#     slug = self.kwargs.get("slug")
#     if slug:
#         queryset = RestaurantLocation.objects.filter(
#                 Q(category__iexact=slug) |
#                 Q(category__icontains=slug)
#             )
#     else:
#         queryset = RestaurantLocation.objects.all()
#     return queryset


# class RestaurantDetailView(DetailView):
#     queryset = RestaurantLocation.objects.all()
    
# def get_object(self, *args, **kwargs):
#     rest_id = self.kwargs.get('rest_id')
#     obj = get_object_or_404(RestaurantLocation, id=rest_id) # pk = rest_id
#     return obj