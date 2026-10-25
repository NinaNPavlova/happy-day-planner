from django.db import models
from django.core.validators import RegexValidator


class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=16, validators=[RegexValidator(regex=r'^\+?\d{9,15}$')])
    year_of_birth = models.PositiveSmallIntegerField(null=True, blank=True)
    celebrations = models.ManyToManyField(
        'celebrations.Celebration',
        blank=True,
        related_name='people',
    )

    def __str__(self):
        return f'{self.name} {self.surname}'


