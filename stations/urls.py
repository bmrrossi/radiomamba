from django.urls import path

from . import views

app_name = 'stations'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:station_id>/', views.detail, name='detail'),
    path('form/', views.form, name='form'),
    path('create/', views.create, name='create'),
    path('delete/<int:station_id>', views.delete, name='delete')
]