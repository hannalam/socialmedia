from django.contrib import admin

# I wrote this code

from .models import Profile, FriendList

# Redesign the models
admin.site.site_header = 'Social network -- Life Share Web Administration'
admin.site.site_title = 'Build a social network'
admin.site.index_title = 'Manange User Data'


# Redesign the costume header and title
class ProfileAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'Default Category'
    list_display = ('user', 'photo',)
    search_fields = ('user',)
    actions = ('change_category_to_default',)
    list_editable = ('photo',)


# Register models
admin.site.register(Profile, ProfileAdmin)
admin.site.register(FriendList)

# end of code I wrote
