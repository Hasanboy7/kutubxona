from django.contrib import admin
from .models import *
# Register your models here.
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email')
    search_fields = ('first_name','last_name','email')
    list_editable = ('email',)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id','name','addres')
    search_fields = ('name','addres',)
    list_display_links = ('name','addres')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','user','place','stars_give')
    search_fields = ('stars_give',)

class PlaceOwnerAdmin(admin.ModelAdmin):
    list_display = ('id','place','owner')
    search_fields = ('place','owner')


admin.site.register(Place,PlaceAdmin)
admin.site.register(Owner,OwnerAdmin)
admin.site.register(PlaceOwner,PlaceOwnerAdmin)
admin.site.register(Comment,CommentAdmin)
