from django.urls import path

from .views import register_view, stats_view

urlpatterns = [
    path("stats/", stats_view, name="stats"),
    path("register/", register_view, name="register"),
]