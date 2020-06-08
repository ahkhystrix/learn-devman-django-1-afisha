from django.contrib import admin

from .models import Feature, Image


class ImageAdmin(admin.TabularInline):
    model = Image
    fields = ("image", "position")


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    inlines = [
        ImageAdmin,
    ]
