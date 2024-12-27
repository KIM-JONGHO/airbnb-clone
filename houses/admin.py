from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "description",
        "address",
        "pets_allowed",
    )

    list_filter = (
        "price",
        "pets_allowed",
    )

    search_fields = (
        "address",
    )

    fields = (
        "name",
        ("price",
        "address",),
        ("description",
        "pets_allowed",),
    )

    list_editable = (
        "pets_allowed",
    )