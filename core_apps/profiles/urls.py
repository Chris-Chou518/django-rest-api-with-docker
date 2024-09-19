from django.urls import path

from .views import (
    ProfileListAPIView,
    ProfileDetailAPIView,
    UpdateProfileAPIView,
    FollowerListView,
    FollowingListView,
    FollowAPIView,
    UnfollowAPIView,
)

urlpatterns = [
    path("all/", ProfileListAPIView.as_view(), name="all-profiles"),
    path("me/", ProfileDetailAPIView.as_view(), name="my-profiles"),
    path("me/update/", UpdateProfileAPIView.as_view(), name="update-profiles"),
    path("me/followers/", FollowerListView.as_view(), name="followers"),
    path("<uuid:user_id>/followings/", FollowingListView.as_view(), name="followings"),
    path("<uuid:user_id>/follow/", FollowAPIView.as_view(), name="follow"),
    path("<uuid:user_id>/unfollow/", UnfollowAPIView.as_view(), name="unfollow"),
]