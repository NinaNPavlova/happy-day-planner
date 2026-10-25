import calendar
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Celebration(models.Model):
    title = models.CharField(max_length=50)
    day = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    month = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    names = models.CharField(max_length=255)

    class Meta:
        unique_together = [['title', 'day', 'month']]
        ordering = ['month', 'day']

    def __str__(self):
        return f'{self.title} ({self.day}/{self.month})'

    def clean(self):
        if self.day and self.month:
            max_day = calendar.monthrange(2000, self.month)[1]
            if self.day > max_day:
                raise ValidationError({
                    'day': f'Month {self.month} no day {self.day}.'
                })


class People(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    circle = models.ForeignKey(
        Circle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='people',
    )
    birthday = models.DateField(null=True, blank=True)
    name_days = models.ManyToManyField(NameDay, blank=True, related_name='contacts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Gift(models.Model):
    class Occasion(models.TextChoices):
        NAME_DAY = 'name_day', 'Name Day'
        BIRTHDAY = 'birthday', 'Birthday'
        OTHER = 'other', 'Other'

    class Status(models.TextChoices):
        IDEA = 'idea', 'Идея'
        GIFTED = 'gifted', 'Gifted'

    title = models.CharField(max_length=50)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='gift_ideas')
    occasion = models.CharField(max_length=20, choices=Occasion.choices)
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.IDEA)
    link = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title} → {self.contact}'