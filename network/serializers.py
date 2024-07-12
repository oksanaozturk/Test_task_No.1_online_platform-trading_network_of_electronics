from rest_framework import serializers

from network.models import Product, NetworkObject


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
        fields = "__all__"


class NetworkObjectDetailSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Course (вывод детальной информации по одному объекту).
    """

    # Задаем новое поле для модели. которое будет передаваться через Serializer
    count_products_for_networkobject = serializers.SerializerMethodField()
    # product_name = serializers.CharField(source="product.name", read_only=True)
    # product_model = serializers.CharField(source="product.model", read_only=True)
    # product_launch_date = serializers.CharField(source="product.launch_date", read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    @staticmethod
    def get_count_products_for_networkobject(networkobject):
        """
        Метод для получения количества продуктов, входящих в networkobject.
        """

        return networkobject.products.count()

    class Meta:
        model = NetworkObject
        fields = "__all__"