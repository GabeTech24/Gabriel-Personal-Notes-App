from django.shortcuts import render
from .models import Notes

# Create your views here.

def notes_list(request):
    return render(request, 'notes/templates/home.html')

def add_note(request):
    return render(request, 'notes/templates/add_note.html')

def note_detail (request):
    return render(request,'notes/templates/note_detail.html')

