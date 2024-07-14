from rest_framework import permissions


class IsActiveAndIsStaff(permissions.BasePermission):
    """
   Класс для проверки является ли Пользователь Активным (is_active) Сотрудником (is_staff)
    """

    message = "Вы не являетесь активным сотрудником или данное поле нельзя изменить"

    def has_permission(self, request, view):
        """
        Метод проверки на то, что пользователь is_active и is_staff.
        """
        return request.user.is_active and request.user.is_staff

    # def has_object_permission(self, request, view, obj):
    #     """
    #     Метод Запрета на редактирование поля debt_to_provider.
    #     """

        # if obj.debt_to_provider != request.obj.debt_to_provider:
        #     print("Поле debt_to_provider не подлежит изменению")
        #     return False

        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if obj.debt_to_provider and request.method in ["PUT", "PATCH"]:
        #     return False

        # Write permissions are only allowed to the owner of the snippet.
        # return obj.debt_to_provider
