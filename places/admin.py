from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Feature, Image


class ImageAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ("image", "image_preview", "position")
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        try:
            return format_html(
                '<img src="{}" width={}/>',
                obj.image.url,
                200,
            )
        except Exception as err:
            print(err)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    inlines = [
        ImageAdmin,
    ]
