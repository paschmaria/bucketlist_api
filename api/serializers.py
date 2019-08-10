from django.contrib.auth.models import User
from rest_framework import serializers

from .models import BucketList

class BucketListSerializer(serializers.ModelSerializer):
  """Serializer to map the model instance into a JSON format"""

  # set owner to readonly field
  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    """Meta class to map the serializer's with the model's fields"""

    model = BucketList
    fields = (
      'id',
      'owner',
      'name',
      'date_created',
      'date_modified'
    )
    read_only_fields = (
      'date_created',
      'date_modified'
    )

class UserSerializer(serializers.ModelSerializer):
  """A user serializer to aid in authentication and authorization."""

  bucketlists = serializers.PrimaryKeyRelatedField(
      many=True, queryset=BucketList.objects.all())

  class Meta:
    """Map this serializer to the default django user model."""

    model = User
    fields = (
      'id',
      'username',
      'bucketlists')