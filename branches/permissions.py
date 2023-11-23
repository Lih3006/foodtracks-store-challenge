from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Branch


class IsStateManager(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, obj: Branch):
        print("State", obj)
        print(req.data)
        return req.user.branch_state == obj.state


class IsCityManager(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, obj: Branch):
        print("City", obj)
        print(req.data)
        return req.user.branch_city == obj.city


class IsSiteManager(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, obj: Branch):
        print("Site", obj)
        print(req.data)
        if req.user.branches.length == 1:
            return req.user.branches[0] == obj
