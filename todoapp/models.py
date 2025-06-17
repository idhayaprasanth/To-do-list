from django.db import models

# Create your models here.
class task(models.Model):
    title=models.CharField(max_length =200)
    description=models.TextField()
    date =models.DateField()
    time =models.TimeField()
    STATUS_CHOICES = [
        ('Pending','Pending'),
        ('Completed','Completed'),
        ('In Progress','In Progress'),
    ]
    task_status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='p')
    created_at = models.DateField(auto_now_add=True)
    priority = models.BooleanField()

    def __str__(self):
        return self.title