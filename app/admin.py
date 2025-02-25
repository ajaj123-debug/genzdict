from django.contrib import admin
from .models import SlangWord

@admin.register(SlangWord)
class SlangWordAdmin(admin.ModelAdmin):
    list_display = ('word', 'definition', 'created_at')
    search_fields = ('word', 'definition')
