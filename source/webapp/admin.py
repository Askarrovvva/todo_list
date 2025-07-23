from django.contrib import admin

from webapp.models import Issue, Status, Type, Project


class TypeInline(admin.TabularInline):
    model = Issue.types.through


class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'statuses', 'summary', 'created_at', 'updated_at']
    list_filter = ['statuses', 'id', 'statuses']
    list_display_links = ["description", 'statuses']
    search_fields = ['description', 'statuses']
    fields = ['description', 'statuses']
    inlines = [
        TypeInline,
    ]

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']
    list_display_links = ['title']
    search_fields = ['title', 'description']
    fields = ['title', 'description', 'start_date', 'end_date']


admin.site.register(Issue, IssueAdmin)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)