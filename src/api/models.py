from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=120)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __sef__(self):
        return self.title