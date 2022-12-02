from django.db import models

CATEGORY = (
    ('Finished', 'Finished'),
    ('Not Finished', 'Not Finished')
)

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, null=True)
    is_finished = models.CharField(max_length=20, choices=CATEGORY, null=True)
    created_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    due_date = models.DateField(null=True, blank=True)
    due_time = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title


