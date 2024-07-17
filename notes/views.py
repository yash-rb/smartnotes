from django.forms import BaseModelForm
from django.shortcuts import render
from .models import Notes
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin


class NotesCreateView(CreateView):
       model = Notes
       template_name = "notes/notes_form.html"
       form_class = NotesForm
       success_url = '/smart/notes'

       def form_valid(self, form):
              self.object = form.save(commit=False)
              self.object.user = self.request.user
              self.object.save()
              return HttpResponseRedirect(self.get_success_url())

class NotesUpdateView(UpdateView):
       model = Notes
       form_class = NotesForm
       success_url = '/smart/notes'

class NotesDeleteView(DeleteView):
       model = Notes
       success_url = '/smart/notes'
       template_name = 'notes/notes_delete.html'


class NotesListView(LoginRequiredMixin, ListView):
       model = Notes
       context_object_name = "notes"
       template_name = "notes/notes_list.html"
       login_url = '/admin'

       def get_queryset(self):
              return self.request.user.notes.all()



# def detail(request, pk):
#         try:
#             note = Notes.objects.get(pk = pk)
#         except Notes.DoesNotExist:
#                raise Http404("The note doesn't exists")
#         return render(request, 'notes/notes_detail.html',{'note': note})

class NotesDetailView(DetailView):
       model = Notes
       context_object_name = "note"