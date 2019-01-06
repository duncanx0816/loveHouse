from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView, DeleteView
from braces.views import LoginRequiredMixin

from .models import Wish
from .forms import NewWishForm


def showList(request):
    pass


class WishMixin(LoginRequiredMixin):
    model = Wish
    login_url = '/login/'


class NewWish(WishMixin, CreateView):
    fields = ['body']
    template_name = 'wish/new.html'

    def post(self, request, *args, **kargs):
        form = NewWishForm(data=request.POST)
        if form.is_valid():
            new_wish = form.save(commit=False)
            new_wish.author = self.request.user
            new_wish.save()
            return redirect('wish:list_wish')
        return self.render_to_response({"form": form})


class ListWish(WishMixin, ListView):
    context_object_name = "wishes"
    template_name = 'wish/list.html'

    def get_queryset(self):
        qs = super(ListWish, self).get_queryset()
        return qs  # .filter(author=self.request.user)
