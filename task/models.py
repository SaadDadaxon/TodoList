from django.db import models
from .constants import TASK


class Task(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=228)
    status = models.IntegerField(choices=TASK.STATUS.CONSTANTS, default=TASK.STATUS.DEFAULT)
    priority = models.IntegerField(choices=TASK.PRIORITY.CONSTANTS, default=TASK.PRIORITY.DEFAULT)
    deadline = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-priority', '-created_date')





