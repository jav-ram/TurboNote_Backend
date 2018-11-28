from django.db.models import Q

from . import models

from rest_framework import permissions


class IsOwnerOrShared(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == 'list':
            return True
        return (request.user == obj.owner.owner) and request.user.is_authenticated


