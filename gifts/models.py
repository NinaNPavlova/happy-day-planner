from django.db import models


class Gift(models.Model):
    person = models.ForeignKey(
        'contacts.Person',
        on_delete=models.CASCADE,
        related_name='gifts',
    )
    gift = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['person', 'gift'],
                name='unique_gift_per_person',
                violation_error_message='This person already has this gift.',
            ),
        ]

    def __str__(self):
        return f'{self.gift} → {self.person}'