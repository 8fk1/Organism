from django.urls import path
from . import views

app_name = "favorite"

urlpatterns = [
    path('', views.favorite_list, name="list"),
    path('<str:name_en>/delete', views.favorite_delete, name="delete")
]
