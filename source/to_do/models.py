from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW', 'Новая'
        IN_PROGRESS = 'IN_PROGRESS', 'В прогрессе'
        DONE = 'DONE', 'Сделано'

    title = models.CharField(max_length=100)
    description = models.TextField()
    detail_description = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices)
    status = models.CharField(
        max_length=11,
        choices=Status.choices,
        default=Status.NEW,
    )
    date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
