from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions

from .models import BucketList
from .permissions import IsOwner
from .serializers import BucketListSerializer, UserSerializer

class CreateView(generics.ListCreateAPIView):
  """This Class defines the create behaviour of our rest API"""

  queryset = BucketList.objects.all()
  serializer_class = BucketListSerializer
  """restrict bucketlist access to authenticated users who are owners only"""
  permission_classes = (
    permissions.IsAuthenticated,
    IsOwner)

  def perform_create(self, serializer):
    """Save the post data when creating a bucketlist."""
    serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
  """This class handles the http GET, PUT and DELETE requests."""

  queryset = BucketList.objects.all()
  serializer_class = BucketListSerializer
  """restrict bucketlist access to authenticated users who are owners only"""
  permission_classes = (
    permissions.IsAuthenticated,
    IsOwner)

class UserView(generics.ListAPIView):
  """View to list the user queryset."""
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
  
class UserDetailsView(generics.RetrieveAPIView):
  """View to retrieve a user instance."""
  queryset = User.objects.all()
  serializer_class = UserSerializer