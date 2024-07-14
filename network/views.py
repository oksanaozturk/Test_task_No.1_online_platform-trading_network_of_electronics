from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from network.models import NetworkObject, Product
from network.serializers import (NetworkObjectDetailSerializer,
                                 NetworkObjectSerializer, ProductSerializer)
from users.permissions import IsActiveAndIsStaff


class ProductViewSet(ModelViewSet):
    """
    Класс настройки CRUD для модели Product с помощью метода ViewSet
    Create, Update, Retrieve, Delete.
    """

    serializer_class = ProductSerializer
    # Получаем все данне из БД
    queryset = Product.objects.all()

    def get_permissions(self):
        """
        Метод для проверки доступа к функцианалу сайта, в зависимости от роли Пользователя.
        """
        if self.action in ["create", "retrieve", "list", "partial_update", "update"]:
            self.permission_classes = (IsActiveAndIsStaff,)
        elif self.action == "destroy":
            self.permission_classes = (IsAdminUser,)

        return super().get_permissions()


class NetworkObjectViewSet(ModelViewSet):
    """
    Класс настройки CRUD для модели NetworkObject с помощью метода ViewSet
    Create, Update, Retrieve, Delete.
    """

    serializer_class = NetworkObjectSerializer
    queryset = NetworkObject.objects.all()
    filterset_fields = ("country",)

    def get_serializer_class(self):
        """
        Метод получения сериализатора в зависимости от запроса
        (вывод всего списка или просмотр одного объекта).
        """

        if self.action == "retrieve":
            return NetworkObjectDetailSerializer

        return NetworkObjectSerializer

    def get_permissions(self):
        """
        Метод для проверки доступа к функцианалу сайта, в зависимости от роли Пользователя.
        """
        if self.action in ["create", "retrieve", "list"]:
            self.permission_classes = (IsActiveAndIsStaff,)
        elif self.action in ["partial_update", "update"]:
            self.permission_classes = (IsActiveAndIsStaff,)
        elif self.action == "destroy":
            self.permission_classes = (IsAdminUser,)

        return super().get_permissions()
