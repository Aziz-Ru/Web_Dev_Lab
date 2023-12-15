from django.urls import path
from . import views
urlpatterns = [
   path('', views.indexes,name=''),
   path('about/', views.indexes,name='about'),
   path('services/', views.indexes,name='services'),
   path('projects/', views.indexes,name='project'),
   path('enroll/', views.indexes,name='enroll'),
]