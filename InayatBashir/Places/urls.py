from django.urls import path
from . import views
app_name = 'places'
urlpatterns = [
    path('', views.AllPlacesList.as_view(), name='all_places_list'),
    path('places/list/<int:pk>/', views.DetailPlace.as_view(), name='detail_place')
]