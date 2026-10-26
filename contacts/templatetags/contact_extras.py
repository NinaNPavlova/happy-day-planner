from datetime import date
from django import template

register = template.Library()
current_year = date.today().year


@register.filter
def person_age(year):
    if not year or year > current_year:
        return 'unknown'
    return current_year - year