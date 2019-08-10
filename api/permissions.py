from rest_framework.permissions import BasePermission

from .models import BucketList

class IsOwner(BasePermission):
  """Custom Permission Class to allow only Bucket list owners to edit them."""

  def has_object_permission(self, request, view, obj):
    """Return True if permission is granted to the Bucket list owner"""
    if isinstance(obj, BucketList):
      return obj.owner == request.user
    return obj.owner == request.user