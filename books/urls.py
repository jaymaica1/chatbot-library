from django.urls import path

from .views import LivroListView, LivroDetailView


urlpatterns = [
    path("books/", LivroListView.as_view(), name="book-list"),
    path(
        "books/<int:pk>/",
        LivroDetailView.as_view(),
        name="book-detail"
    ),
]