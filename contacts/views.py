from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)

from .forms import PersonForm
from .models import Person


class PersonListView(ListView):
    model = Person
    template_name = 'contacts/contact_list.html'
    context_object_name = 'people'


class PersonDetailView(DetailView):
    model = Person
    template_name = 'contacts/contact_detail.html'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'contacts/contact_form.html'
    success_url = reverse_lazy('contacts:list')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'contacts/contact_form.html'
    success_url = reverse_lazy('contacts:list')


class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'contacts/contact_confirm_delete.html'
    success_url = reverse_lazy('contacts:list')