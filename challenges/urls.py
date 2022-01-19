from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index),
    # path("january", views.january),
    # path("february", views.february),
    # now we need to pass dynamic urls
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_chllenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
