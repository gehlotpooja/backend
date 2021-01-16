from django.urls import path
from . import views
urlpatterns = [
    path(r'lobby_creation/',views.lobby_creation_api),
    path(r'adding_member/',views.adding_member_api),
    path(r'check_winner/',views.check_winner_api),
    path(r'dashboard/',views.dashboard_api),
]