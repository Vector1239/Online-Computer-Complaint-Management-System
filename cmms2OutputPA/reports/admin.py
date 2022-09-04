from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Student)
admin.site.register(Block)
admin.site.register(Lab)
admin.site.register(Computer)
admin.site.register(Report)