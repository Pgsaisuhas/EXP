from django.contrib import admin
from . import models


# * Registered 2 main models for admin panel access.

admin.site.register(models.Profile)
admin.site.register(models.Expense)