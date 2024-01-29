from django.contrib import admin

# I wrote this code

from .models import Status

# Redesign the costume header and title


class StatusAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'Default Category'
    list_display = ('user', 'title', 'caption', 'date',)
    search_fields = ('caption',)
    actions = ('change_category_to_default',)
    list_editable = ('title', 'caption',)


# Register models
admin.site.register(Status, StatusAdmin)


# end of code I wrote
