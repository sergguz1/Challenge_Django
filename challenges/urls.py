from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    path("",views.index, name="index"), #/challenges/
    path("<int:month>", views.monthly_challenges_by_number),
    path("<str:month>", views.monthly_challenge, name="month-string")
]
