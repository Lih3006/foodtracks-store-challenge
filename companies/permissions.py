from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Company


class IsAdminAndAccountOwner(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, obj: Company):
        return req.user.is_superuser and req.user.id == obj.owner.id
