from django.db import models


class Product(models.Model):
    """
    Класс модели продукта.
    """

    name = models.CharField(max_length=150, verbose_name="Название продукта", help_text="Введите название продукта")
    model = models.CharField(max_length=150, verbose_name="Модель продукта", help_text="Введите модель продукта",
                             blank=True, null=True)
    launch_date = models.DateField(auto_now_add=True, verbose_name="Дата выхода продукта на рынок",
                                   help_text="Введите дату выхода продукта на рынок")

    # provider = models.ForeignKey("NetworkObject", verbose_name="Поставщик", related_name="products",
    #     on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class NetworkObject(models.Model):
    """
    Класс модели объекта сети.
    """

    name = models.CharField(max_length=100, verbose_name="Название объекта сети",
                            help_text="Введите название объекта сети" )
    email = models.EmailField(verbose_name="Email", help_text="Введите email", blank=True, null=True)
    country = models.CharField(max_length=50, verbose_name="Страна", help_text="Введите назание страны",
                               blank=True, null=True)
    town = models.CharField(max_length=50, verbose_name="Город", help_text="Введите назание города",
                            blank=True, null=True)
    street = models.CharField(max_length=100, verbose_name="Улица", help_text="Введите назание улицы",
                              blank=True, null=True)
    house = models.PositiveIntegerField(verbose_name="Номер дома", help_text="Введите номер дома",
                                        blank=True, null=True)
    products = models.ForeignKey(Product, verbose_name="Продукты", blank=True, null=True, on_delete=models.CASCADE)

    provider = models.ForeignKey("NetworkObject", verbose_name="Поставщик", on_delete=models.CASCADE,
                                 help_text="Укажите поставщика")
    debt_to_provider = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Долг перед поставщиком",
                                           help_text="Введите долг перел Поставщиком",
                                           blank=True, null=True)
    time_of_creation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Объект сети"
        verbose_name_plural = "Объекты сети"

    def __str__(self):
        return self.name
