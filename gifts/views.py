from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)

from .forms import GiftForm
from .models import Gift

class GiftListView(ListView):
    model = Gift
    template_name = 'gifts/gift_list.html'
    context_object_name = 'gifts'


class GiftDetailView(DetailView):
    model = Gift
    template_name = 'gifts/gift_detail.html'


class GiftCreateView(CreateView):
    model = Gift
    form_class = GiftForm
    template_name = 'gifts/gift_form.html'
    success_url = reverse_lazy('gifts:list')


class GiftUpdateView(UpdateView):
    model = Gift
    form_class = GiftForm
    template_name = 'gifts/gift_form.html'
    success_url = reverse_lazy('gifts:list')


class GiftDeleteView(DeleteView):
    model = Gift
    template_name = 'gifts/gift_confirm_delete.html'
    success_url = reverse_lazy('gifts:list')