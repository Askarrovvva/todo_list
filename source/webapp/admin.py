from django.contrib import admin

from webapp.models import ToDo # noqa: F401


class ToDoAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date_completion']
    list_filter = ['status', 'id']
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'date_completion']



admin.site.register(ToDo, ToDoAdmin)
