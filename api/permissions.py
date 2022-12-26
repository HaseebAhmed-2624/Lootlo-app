from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the object
        return obj.id == request.user.id or request.user.is_staff
