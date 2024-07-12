from rest_framework.viewsets import ModelViewSet

from network.models import NetworkObject, Product
from network.serializers import (NetworkObjectDetailSerializer,
                                 NetworkObjectSerializer, ProductSerializer)


class ProductViewSet(ModelViewSet):
    """
    Класс настройки CRUD для модели Product с помощью метода ViewSet
    Create, Update, Retrieve, Delete.
    """

    serializer_class = ProductSerializer
    # Получаем все данне из БД
    queryset = Product.objects.all()


class NetworkObjectViewSet(ModelViewSet):
    """
    Класс настройки CRUD для модели NetworkObject с помощью метода ViewSet
    Create, Update, Retrieve, Delete.
    """

    serializer_class = NetworkObjectSerializer
    queryset = NetworkObject.objects.all()

    def get_serializer_class(self):
        """
        Метод получения сериализатора в зависимости от запроса
        (вывод всего списка или просмотр одного объекта).
        """

        if self.action == "retrieve":
            return NetworkObjectDetailSerializer

        return NetworkObjectSerializer
