from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView, DeleteView
from braces.views import LoginRequiredMixin, CsrfExemptMixin
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


from random import randint, shuffle
from logzero import logger

from .models import Note
from .forms import NewNoteForm


class NoteMixin(CsrfExemptMixin, LoginRequiredMixin):
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
        return qs  # .filter(author=self.request.user)

    def get_context_data(self, *args, **kargs):
        context = super().get_context_data(*args, **kargs)
        context['left'] = randint(0, 30)
        context['top'] = randint(0, 30)
        return context

    def post(self, request):
        res = []
        for note in self.get_queryset().order_by('-created')[:9]:
            res.append({
                'gender': note.gender,
                'left': randint(-30, 30),
                'top': randint(-15, 15),
                'body': note.body
            })
        logger.info(len(res))
        logger.info(res)
        shuffle(res)
        return JsonResponse(res, safe=False)


class HistNote(NoteMixin, ListView):
    context_object_name = "notes"
    template_name = 'note/history.html'

    def get_queryset(self):
        qs = super(HistNote, self).get_queryset()
        return qs  # .filter(author=self.request.user)
