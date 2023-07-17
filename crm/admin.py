from atexit import register
from django.contrib import admin
from .models import *

admin.site.register(Table),
admin.site.register(Lead),
admin.site.register(LeadComment),