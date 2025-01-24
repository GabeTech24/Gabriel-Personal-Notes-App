from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('', views.add_note, name='add_note'),
    path('', views.note_detail, name='note_detail'),
]
