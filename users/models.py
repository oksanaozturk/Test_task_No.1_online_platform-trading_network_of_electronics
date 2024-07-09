from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс для создания модели Пользователя"""

    username = None

    email = models.EmailField(
        max_length=150, unique=True, verbose_name="email", help_text="Введите email"
    )
    first_name = models.CharField(max_length=50, verbose_name="Имя", blank=True, null=True,
                                  help_text="Напишите Ваше имя")
    second_name = models.CharField(max_length=50, verbose_name="Имя", blank=True, null=True,
                                  help_text="Напишите Вашу фамилию")

    # Выбираем полем для авторизации email
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
