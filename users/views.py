from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """Класс для настройки CRUD для модели User с помощью метода ViewSet
    Create, Update, Retrieve, Delete."""

    serializer_class = UserSerializer
    # Получаем все данне из БД
    queryset = User.objects.all()

    def perform_create(self, serializer):
        """
        Данный метод необходим для того, чтобы нам не мешала настройка 'username = None',
        указанная нами в модели User в models.py
        """

        user = serializer.save(is_active=True)
        # Кешируем обязательно пароль Пользователя
        user.set_password(user.password)
        user.save()
