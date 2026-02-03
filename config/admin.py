from django.contrib import admin
from .models import Quest, DailyProgress

@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'order')

@admin.register(DailyProgress)
class DailyProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'quest', 'date', 'is_completed')