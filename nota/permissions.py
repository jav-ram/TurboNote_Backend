from django.db.models import Q

from . import models

from rest_framework import permissions


class IsOwnerOrShared(permissions.BasePermission):
    def can_access_note(self, request, view, obj):
        return models.Shared.objects.filter(
            Q(note__owner__owner=request.user, note=obj) |
            Q(shared_to=request.user, note=obj) |
            Q(owner=request.user, note=obj)
        ).exist()


