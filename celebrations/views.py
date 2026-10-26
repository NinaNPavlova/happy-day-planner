from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView,
)

from .forms import CelebrationForm
from .models import Celebration
import calendar
from datetime import date
from django.views.generic import TemplateView


class CelebrationListView(ListView):
    model = Celebration
    template_name = 'celebrations/celebration_list.html'
    context_object_name = 'celebrations'

    def get_queryset(self):
        queryset = super().get_queryset()
        celebration_type = self.request.GET.get('type')
        if celebration_type:
            queryset = queryset.filter(celebration_type = celebration_type)
        sort = self.request.GET.get('sort')
        if sort == 'title':
            queryset = queryset.order_by('title')
        return queryset


class CelebrationDetailView(DetailView):
    model = Celebration
    template_name = 'celebrations/celebration_detail.html'


class CelebrationCreateView(CreateView):
    model = Celebration
    form_class = CelebrationForm
    template_name = 'celebrations/celebration_form.html'
    success_url = reverse_lazy('celebrations:list')

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()
        year = int(self.request.GET.get('year', today.year))
        month = int(self.request.GET.get('month', today.month))
        celebrations_by_day = {}
        celebrations = Celebration.objects.filter(month=month)
        if month == 1:
            prev_year, prev_month = year - 1, 12
        else:
            prev_year, prev_month = year, month - 1

        if month == 12:
            next_year, next_month = year + 1, 1
        else:
            next_year, next_month = year, month + 1
        for celebration in celebrations:
            celebrations_by_day.setdefault(celebration.day_of_month, []).append(celebration)
        grid = []
        for week in calendar.monthcalendar(year, month):
            row = []
            for number in week:
                if number == 0:
                    row.append(None)
                else:
                    row.append({
                        'day': number,
                        'celebrations': celebrations_by_day.get(number, []),
                        'is_today': number == today.day and month == today.month and year == today.year,
                    })
            grid.append(row)
        context.update({'weeks': grid, 'year': year, 'month': month, 'month_name': calendar.month_name[month], 'prev_year': prev_year, 'prev_month': prev_month, 'next_year': next_year, 'next_month': next_month,})
        return context


