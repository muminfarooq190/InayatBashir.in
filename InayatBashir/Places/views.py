
from django.shortcuts import render
from core.models import Places
from django.views.generic import (ListView, DetailView)

class AllPlacesList(ListView):
    model = Places
    template_name = 'Places/places_list.html'
    context_object_name = 'places'

    def get_queryset(self):
        return Places.objects.all()

class DetailPlace(DetailView):
    model = Places 
    template_name = 'Places/places_detail.html'
    context_object_name = 'place'       
