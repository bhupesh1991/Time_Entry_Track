from django.contrib import admin
from timetrack.models import Project,Task
# Register your models here.


admin.site.register(Task)
admin.site.register(Project)