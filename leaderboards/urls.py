from django.urls import path
from .views import (
    LeaderboardView,
    LogoutView,
    LoggedOutView,
    RegisterView,
    RunningActivityCreateView,
    RunningActivityDeleteView,
    RunningActivityListView,
    RunningActivityUpdateView,
)


urlpatterns = [
    path("", RunningActivityListView.as_view(), name="activity-list"),
    path(
        "leaderboard/", LeaderboardView.as_view(), name="leaderboard"
    ),  # <-- Add this path
    path(
        "create/", RunningActivityCreateView.as_view(), name="create-running-activity"
    ),
    path(
        "<int:pk>/delete/",
        RunningActivityDeleteView.as_view(),
        name="delete-running-activity",
    ),
    path(
        "<int:pk>/update/",
        RunningActivityUpdateView.as_view(),
        name="edit-running-activity",
    ),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("logged-out/", LoggedOutView.as_view(), name="logged-out"),
]
