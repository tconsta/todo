from django.db import models


class Task(models.Model):
    """Model representing a task."""
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000,
                                   help_text='Enter a description of the task',
                                   null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
