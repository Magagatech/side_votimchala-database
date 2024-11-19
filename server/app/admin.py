from django.contrib import admin
from .models import Student, Roles, Candidate, Election, Position, Vote

# Register your models here.
admin.site.register([Student, Roles, Candidate, Election, Position, Vote])
