from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView, DeleteView
from braces.views import LoginRequiredMixin

from .models import Note
from .forms import NewNoteForm


class NoteMixin(LoginRequiredMixin):
    model = Note
    login_url = '/login/'


class NewNote(NoteMixin, CreateView):
    fields = ['body']
    template_name = 'note/new.html'

    def post(self, request, *args, **kargs):
        form = NewNoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.author = self.request.user
            new_note.save()
            return redirect('note:list_note')
        return self.render_to_response({"form": form})


class ListNote(NoteMixin, ListView):
    context_object_name = "notes"
    template_name = 'note/manage.html'

    def get_queryset(self):
        qs = super(ListNote, self).get_queryset()
        return qs.filter(author=self.request.user)


class HistNote(NoteMixin, ListView):
    context_object_name = "notes"
    template_name = 'note/history.html'

    def get_queryset(self):
        qs = super(HistNote, self).get_queryset()
        return qs.filter(author=self.request.user)
