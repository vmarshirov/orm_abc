from django.urls import path

from . import views

app_name = 'orm_abc_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('datetime_nov/', views.datetime_nov, name='datetime_nov'),
    path('var_list_dict/', views.var_list_dict, name='var_list_dict'),
    path('abc_form/', views.abc_form, name='abc_form'),
    path('abc_get/', views.abc_get, name='abc_get'),
    path('abc_model_form/', views.abc_model_form, name='abc_model_form'),
    path('abc_tweaks_form/', views.abc_tweaks_form, name='abc_tweaks_form'),
    path('abc_result/', views.abc_result, name='abc_result'),
    path('table/', views.table, name='table'),
]
