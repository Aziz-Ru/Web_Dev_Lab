from django.urls import path
from . import views
urlpatterns = [
   path('', views.home),
   path('about/', views.about),
   path('services/', views.services),
   path('project/', views.project),
]