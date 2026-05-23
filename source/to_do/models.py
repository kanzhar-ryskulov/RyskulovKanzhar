from django.db import models

# Create your models here.


class Task(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW', 'Новая'
        IN_PROGRESS = 'IN_PROGRESS', 'В прогрессе'
        DONE = 'DONE', 'Сделано'

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=11,
        choices=Status.choices,
        default=Status.NEW,
    )
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
