from django.contrib import admin
from .models import User,FriendRequest

# Register your models here.
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'form_user', 'to_user')
    list_display_links = ('id', 'to_user')

admin.site.register(FriendRequest, FriendRequestAdmin)

admin.site.register(User)
