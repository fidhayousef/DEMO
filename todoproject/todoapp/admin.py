import task as task
from django.contrib import admin

from .models import Task

# Register your models here.
admin.site.register(Task)
