from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView, DeleteView
from braces.views import LoginRequiredMixin


class MemoryIndex(TemplateView):
    template_name = 'memory/index.html'
