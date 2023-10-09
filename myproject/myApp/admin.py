from django.contrib import admin
from .models import Movie,Movie_detail

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display=['id','name','year','pic','hit_flop','rating']
admin.site.register(Movie,MovieAdmin)

class MovieDetailAdmin(admin.ModelAdmin):
  list_display=['movie','image','actor_name','actress_name','details']
admin.site.register(Movie_detail,MovieDetailAdmin)