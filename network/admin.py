from django.contrib import admin

from network.models import Product, NetworkObject


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Класс для регистрации  модели Product в админке.
    """

    list_display = ("id", "name", "model", "launch_date")
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(NetworkObject)
class NetworkObjectAdmin(admin.ModelAdmin):
    """
    Класс для регистрации модели NetworkObject в админке.
    """

    list_display = ("id", "name", "email", "country", "town", "provider", "debt_to_provider", "time_of_creation")
    list_filter = ("name",)
    search_fields = ("name", "country")
