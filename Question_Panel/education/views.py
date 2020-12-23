from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .models import Note
from django.contrib.auth.mixins import LoginRequiredMixin


class NoteList(ListView):
    queryset = Note.objects.filter(note_status="publish")
    template_name = "education/note_list.html"
    context_object_name = "notes"


class MyNote(LoginRequiredMixin, ListView):
    model = Note
    template_name = "education/my_note.html"
    context_object_name = "notes"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__in=[self.request.user])


class NoteDetail(DetailView):
    pass


class CreateNote(CreateView, LoginRequiredMixin):
    model = Note
    fields = ["note_title", "note_body", "note_status"]
    template_name = "education/create_note.html"
    success_url = "/education/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateNote, self).form_valid(form)


class UpdateNote(UpdateView, LoginRequiredMixin):
    model = Note
    fields = ['note_title', 'note_body', 'note_status']
    template_name = 'education/create_note.html'
    success_url = "/education/"


class DeleteNote(DeleteView, LoginRequiredMixin):
    pass
