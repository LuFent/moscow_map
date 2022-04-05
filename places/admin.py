from django.contrib import admin
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin
from django.utils.safestring import mark_safe


class ImagesInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image', 'preview', 'number')
    readonly_fields = ("preview",)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

    inlines = [ImagesInline]


