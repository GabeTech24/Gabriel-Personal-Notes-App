from django.shortcuts import render
from .models import Notes

# Create your views here.

def notes_list(request):
    return render(request, 'note/home.html')

def add_note(request):
    return render(request, 'note/add_note.html')

def note_detail (request):
    return render(request,'note/note_detail.html')

