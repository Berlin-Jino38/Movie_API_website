from . import views
from django.urls import path

urlpatterns = [
   path('movies/', views.MovieListCreate.as_view()),
   path('movies/<int:pk>/', views.MovieRetriveUpdateDestroy.as_view())
   
]
