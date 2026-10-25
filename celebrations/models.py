
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Celebration(models.Model):
    class CelebrationType(models.TextChoices):
        BIRTHDAY = 'birthday', 'Birthday'
        NAME_DAY = 'name_day', 'Name day'
        OTHER = 'other', 'Other'

    celebration_type = models.CharField(
        max_length=20,
        choices=CelebrationType.choices,
        default=CelebrationType.BIRTHDAY,
    )
    title = models.CharField(max_length=50, blank=True)
    day_of_month = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    month = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])

    class Meta:
        ordering = ['month', 'day_of_month']

    def __str__(self):
        return f'{self.get_celebration_type_display()} ({self.day_of_month}/{self.month})'

    def clean(self):
        if self.celebration_type == self.CelebrationType.OTHER and not self.title:
            raise ValidationError({'title': 'Please add a title for the celebration.'})