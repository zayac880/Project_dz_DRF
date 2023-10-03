from rest_framework.permissions import BasePermission


class IsManagers(BasePermission):
    message = 'Вы не менеджер!'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in ['POST', 'DELETE']:
                if request.user.is_superuser:
                    return True
                if request.user.is_staff:
                    self.message = 'Менеджер не может создавать и удалять'
                    return False
                return True
            if request.method in ['PUT', 'PATCH', 'DELETE']:
                obj = view.get_object()
                if obj.owner == request.user or request.user.is_staff:
                    return True
                else:
                    self.message = 'Вы не имеете доступ'
            return True
