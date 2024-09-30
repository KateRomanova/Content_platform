from django.contrib import admin

from content.models import Content, Category


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "photo",
        "publication_date",
        "is_content_paid",
        "category",
    )


@admin.register(Category)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
