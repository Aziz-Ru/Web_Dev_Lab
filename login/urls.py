from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name=''),
    path('submit_form/', views.submitForm,name='submit_form'),
]