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

    @staticmethod
    def get_count_products_for_networkobject(networkobject):
        """
        Метод для получения количества продуктов, входящих в networkobject.
        """

        return networkobject.products.count()

    # url_provider = serializers.HyperlinkedIdentityField(view_name='networkobjects-detail', read_only=True)
    # url = serializers.HyperlinkedIdentityField('network:networkobjects-detail',
    #                                            read_only=True)

    class Meta:
        model = NetworkObject
        fields = "__all__"
