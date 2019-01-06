from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView, DeleteView
from braces.views import LoginRequiredMixin

from .models import Todo
from .forms import NewTodoForm


class TodoMixin(LoginRequiredMixin):
    model = Todo
    login_url = '/login/'


class NewTodo(TodoMixin, CreateView):
    fields = ['body']
    template_name = 'todo/new.html'

    def post(self, request, *args, **kargs):
        form = NewTodoForm(data=request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.author = self.request.user
            new_todo.save()
            return redirect('todo:list_todo')
        return self.render_to_response({"form": form})


class ListTodo(TodoMixin, ListView):
    context_object_name = "todoes"
    template_name = 'todo/list.html'

    def get_queryset(self):
        qs = super(ListTodo, self).get_queryset()
        return qs  # .filter(author=self.request.user)
