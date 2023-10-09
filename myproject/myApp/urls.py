from . import views
from django.urls import path

urlpatterns = [
    path('',views.index_view,name='home'),
    path('<str:name>/',views.detail_view,name='details'),
    path('search',views.search_view,name='search'),
    path('signup',views.signup_view,name='signup'),
]
