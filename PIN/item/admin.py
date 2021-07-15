from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'active')
    # readonly_fields = ('slug',)
    # list_display_links = ('name',)
    # search_fields = ('title',)
    list_filter = ('active',)
    # date_hierarchy = 'created'
    # ordering = ('-created',)
    # actions = ('',)
