from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """Allow if user is owner of object or Admin user"""
        return obj.id == request.user.id or request.user.is_staff
