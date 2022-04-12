from django.contrib import admin
from django.urls import path
from TimeToFly.web.views import IndexView, AboutView, NotFoundView, FlightsListView, \
    ChooseFlightView, EditFlightView, DeleteFlightView, CurrentFlightView, CreateFlightView


urlpatterns = (
    path('', IndexView.as_view(), name='show index'),
    path('about/', AboutView.as_view(), name='about us'),
    path('page-not-found/', NotFoundView.as_view(), name='not found'),
    path('flights/', FlightsListView.as_view(), name='show flights'),
    path('flights/choose/', ChooseFlightView.as_view(), name='book flight'),
    path('flights/create/', CreateFlightView.as_view(), name='create flight'),
    path('flights/edit/<int:pk>/', EditFlightView.as_view(), name='update flight'),
    path('flights/delete/<int:pk>/', DeleteFlightView.as_view(), name='delete flight'),
    path('flights/<int:pk>/', CurrentFlightView.as_view(), name='view flight'),
)