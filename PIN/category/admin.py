from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'cat_name', 'active')
    # readonly_fields = ('slug',)
    # list_display_links = ('name',)
    search_fields = ('cat_name',)
    list_filter = ('active',)
    # date_hierarchy = 'created'
    # ordering = ('-created',)
    # actions = ('',)
