from django.contrib import admin
from .models import RunningActivity


@admin.register(RunningActivity)
class RunningActivityAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'activity_date',
        'distance',
        'duration',
        'pace',
        'heart_rate_avg',
        'heart_rate_max',
        'ascent',
        'descent',
        'created_at',
    )
    list_filter = ('activity_date',)
    search_fields = ('user__username', 'activity_date')
