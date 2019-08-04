from django.urls import path
from . import views
urlpatterns = [
    path('guides/', views.guide, name='guide'),
]
