from django.contrib import admin

from .models import Issue


class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'statuses', 'summary']
    list_filter = ['statuses', 'id', 'types']
    list_display_links = ["description"]
    search_fields = ['description', 'statuses']
    fields = ['description', 'statuses']
    readonly_fields = ['types']


admin.site.register(Issue, IssueAdmin)