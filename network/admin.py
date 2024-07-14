from django.contrib import admin

from network.models import NetworkObject, Product

from django.contrib import admin


@admin.action(description="Can clear debt to provider")
def clear_debt_to_provider(modeladmin, request, queryset):
    queryset.update(debt_to_provider=0.00)


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

    list_display = (
        "id",
        "name",
        "email",
        "country",
        "town",
        "provider",
        "debt_to_provider",
        "time_of_creation",
    )
    list_filter = ("name", "town")
    search_fields = ("name", "country")
    actions = [clear_debt_to_provider]
