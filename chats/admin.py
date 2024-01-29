from django.contrib import admin
# I wrote this code

from .models import ChatRoom, ChatRoomMessage


# Redesign the costume header and title
class ChatRoomMessageAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'Default Category'
    list_display = ('user', 'chatroom', 'messages', 'date',)
    search_fields = ('messages',)
    actions = ('change_category_to_default',)


# Register models
admin.site.register(ChatRoom)
admin.site.register(ChatRoomMessage, ChatRoomMessageAdmin)

# end of code I wrote
