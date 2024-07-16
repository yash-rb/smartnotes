from django.shortcuts import render
from .models import Notes
from django.http import Http404

def list(request):
        all_notes = Notes.objects.all()
        return render(request, 'notes/notes_list.html',{'notes':all_notes})

def detail(request, pk):
        try:
            note = Notes.objects.get(pk = pk)
        except Notes.DoesNotExist:
               raise Http404("The note doesn't exists")
        return render(request, 'notes/notes_detail.html',{'note': note})