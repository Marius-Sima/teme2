from django.urls import path
from mainapp import views

urlpatterns = [
    path("", views.Homepage.as_view(), name="home"),
    path("book/<int:pk>", views.BookView.as_view(), name="details"),
    path("add", views.AddBookFormView.as_view(), name="add"),
]
