from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100,unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Task(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, blank=True, null=True)
    due = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    # for_date = models.DateField()
    start = models.DateTimeField()
    end = models.DateTimeField()    
    complete = models.BooleanField(default=False)    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

