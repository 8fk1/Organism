from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'organism'

urlpatterns = [
    path('', views.organism_list, name="list"),
    path('organism/', views.permission_denied, name="permission_denied"),
    path('organism/register', views.organism_register, name="register"),
    path('organism/<str:organism_name_en>',
         views.organism_detail, name='detail'),
    path('organism/<str:organism_name_en>/edit',
         views.organism_edit, name="edit"),
    path('organism/<str:organism_name_en>/delete',
         views.organism_delete, name="delete"),
]
