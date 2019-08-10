from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from .views import CreateView, DetailsView, UserView, UserDetailsView

urlpatterns = [
    path('auth/', include('rest_framework.urls',
                            namespace='rest_framework')),
    path("bucketlists/", CreateView.as_view(), name="create"),
    path('get-token/', obtain_auth_token),
    path('users/', UserView.as_view(), name="users"),

    re_path(r'^bucketlists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    re_path(r'^users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name='user_details'),
]

# append the format to be used to every URL in the pattern
urlpatterns = format_suffix_patterns(urlpatterns)
