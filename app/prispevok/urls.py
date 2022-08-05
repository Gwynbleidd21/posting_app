"""URL mappings for prispevok app"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListPrispevokAPIView.as_view(),
         name="prispevok_list"),
    path("<int:pk>/", views.RetrievePostAPIView.as_view(),
         name="prispevok_list"),
    path("user/<int:pk>/", views.RetrieveUserAPIView.as_view(),
         name="user_prispevok_list"),
    path("create/", views.CreatePrispevokAPIView.as_view(),
         name="prispevok_create"),
    path("update/<int:pk>/", views.UpdatePrispevokAPIView.as_view(),
         name="update_prispevok"),
    path("delete/<int:pk>/", views.DeletePrispevokAPIView.as_view(),
         name="delete_prispevok")
]
