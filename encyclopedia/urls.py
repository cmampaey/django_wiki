from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new_page, name="new"),
    path("wiki/<str:title>", views.entry, name = "entry"),
    # path("random", views.random_page, name="random"),
]
