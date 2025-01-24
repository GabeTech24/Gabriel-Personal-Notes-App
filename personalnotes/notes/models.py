from django.db import models
from django.utils import timezone

# Create your models here.
class Notes (models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

        def __str__ (self):
            return self.title
