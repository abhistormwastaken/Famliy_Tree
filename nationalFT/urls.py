from django.contrib import admin
from django.urls import path
from nationalFT import views

urlpatterns = [
    path("tree", views.FamilyTree.as_view()),
]
