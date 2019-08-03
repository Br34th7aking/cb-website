from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('resource/', views.resource, name='resource'),
    path('about/', views.about_us, name='about'),
]
