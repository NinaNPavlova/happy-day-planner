from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView,
)

from .forms import CelebrationForm
from .models import Celebration


class CelebrationListView(ListView):
    model = Celebration
    template_name = 'celebrations/celebration_list.html'
    context_object_name = 'celebrations'


class CelebrationDetailView(DetailView):
    model = Celebration
    template_name = 'celebrations/celebration_detail.html'


class CelebrationCreateView(CreateView):
    model = Celebration
    form_class = CelebrationForm
    template_name = 'celebrations/celebration_form.html'
    success_url = reverse_lazy('celebrations:list')


