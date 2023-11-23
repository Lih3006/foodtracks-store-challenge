from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Branch
from companies.models import Company


from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Branch


class IsLinkedToBranch(permissions.BasePermission):
    def has_permission(self, req: Request, view: View):
        # Permitir apenas superusuários, gerentes regionais e gerentes de site para criar
        if req.method == "POST":
            return req.user.is_superuser or req.user.role in [
                "regional_manager",
                "site_manager",
            ]
        if req.method == "DELETE":
            return req.user.is_superuser
        # Permitir leitura (GET) para todos os usuários
        return True

    def has_object_permission(self, req: Request, view: View, obj: Branch):
        return (
            req.user.is_superuser
            or req.user.role == "regional_manager"
            and req.user.branches.filter(id=obj.id).exists()
            or req.user.role == "site_manager"
            and req.user.branches.filter(id=obj.id).exists()
        )
