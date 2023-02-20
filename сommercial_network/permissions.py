from rest_framework.permissions import BasePermission


class IsActivePermission(BasePermission):
    """ Доступ только для "активных" пользователей. """

    message = "Этот пользователь не активен. Связаться с администратором."

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
