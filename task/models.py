from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=228)
    content = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





