from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('recipes/',view_recipes_page),
    path('recipesdata/',view_recipes_lists),
    path('recipesform/',view_recipes_form),
    path('recipesform/save',view_recipesdata_save),
    path('recipesdata/edit/<int:ID>',view_recipesdata_updateform),
    path('recipesdata/edit/update/<int:ID>',view_update_form_data_in_db),
    path('register/',view_register_user),
    path('login',view_authenticate_user, name="login"),
    path('logout/',view_logout),

   
]