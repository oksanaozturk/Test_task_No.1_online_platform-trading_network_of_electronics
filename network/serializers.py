from rest_framework import serializers

from network.models import NetworkObject, Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Product.
    """

    class Meta:
        model = Product
        fields = "__all__"


class NetworkObjectSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели NetworkObject.
    """

    class Meta:
        model = NetworkObject
        exclude = ("products",)


class NetworkObjectDetailSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Course (вывод детальной информации по одному объекту).
    """

    # Задаем новое поле для модели, которое будет передаваться через Serializer
    count_products_for_networkobject = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)
    url_provider = serializers.SerializerMethodField()

    @staticmethod
    def get_count_products_for_networkobject(networkobject):
        """
        Метод для получения количества продуктов, входящих в networkobject.
        """

        return networkobject.products.count()

    @staticmethod
    def get_url_provider(networkobject):
        provider = networkobject.provider
        url_provider = f"http://127.0.0.1:8000/network/networkobjects/{provider.pk}/"
        return url_provider

    class Meta:
        model = NetworkObject
        fields = "__all__"
