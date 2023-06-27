from django.contrib import admin

from home.models import Task


@admin.register(Task)
class RaiseShotPriceTicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'date', 'time', 'status')
