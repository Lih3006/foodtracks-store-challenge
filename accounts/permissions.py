from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Account


class IsAdminOrAccountOwner(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, obj: Account):
        return req.user.is_superuser or req.user.email == obj.email
