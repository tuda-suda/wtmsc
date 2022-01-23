from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-match/', views.add_match, name='add_match'),
    path('matches/<int:match_id>/', views.match_view, name='match_view'),
    path('add-vehicle/', views.add_vehicle, name='add_vehicle'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('vehicles/<slug>/', views.vehicle_view, name='vehicle_view')
]
