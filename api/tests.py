from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status 

from.models import BucketList

class ModelTestCase(TestCase):
  """This class defines the test suite for the bucketlist model"""

  def setUp(self):
    """Define the test client and other test variables"""
    user = User.objects.create(username='Nerd')
    self.bucketlist_name = 'Write world class code!'
    self.bucketlist = BucketList(owner=user, name=self.bucketlist_name)

  def test_model_can_create_a_bucket(self):
    """Test that the model can create a bucketlist"""
    old_count = BucketList.objects.count()
    self.bucketlist.save()
    new_count = BucketList.objects.count()
    self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
  """
    Test suite for the api views.

    View objectives:
    Create a bucketlist – Handle POST request
    Read a bucketlist(s) – Handle GET request
    Update a bucketlist – Handle PUT request
    Delete a bucketlist – Handle DELETE request
  """

  def setUp(self):
    """Define the test client and other test variables"""
    user = User.objects.create(username="nerd")
    
    # Initialize client and force it to use authentication
    self.client = APIClient()
    self.client.force_authenticate(user=user)

    # Since user model instance is not serializable, use its Id/PK
    self.bucketlist_data = {'owner': user.id, 'name': 'Go to Ibiza'}
    self.response = self.client.post(
      reverse('create'),
      self.bucketlist_data,
      format='json'
    )

  def test_api_can_create_a_bucketlist(self):
    """Test the API has bucket creation capability."""
    self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

  def test_authorization_is_enforced(self):
    """Test that the api has user authorization."""
    new_client = APIClient()
    res = new_client.get(
      '/bucketlists/', kwargs={'pk': 3},
      format='json')

    self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

  def test_api_can_get_a_bucketlist(self):
    """Test the API can get a given bucketlist"""
    bucketlist = BucketList.objects.get(id=1)
    response = self.client.get(
        '/bucketlists/',
        kwargs={'pk': bucketlist.id}, format="json")

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, bucketlist)

  def test_api_can_update_bucketlist(self):
    """Test the API can update a given bucketlist"""
    bucketlist = BucketList.objects.get()
    change_bucketlist = {'name': 'Something new'}
    res = self.client.put(
      reverse('details', kwargs={'pk': bucketlist.id}),
      change_bucketlist, format='json'
    )
    
    self.assertEqual(res.status_code, status.HTTP_200_OK)

  def test_api_can_delete_bucketlist(self):
    """Test the API can delete a given bucketlist"""
    bucketlist = BucketList.objects.get()
    response = self.client.delete(
      reverse('details', kwargs={'pk': bucketlist.id}),
      format='json', follow=True
    )

    self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
