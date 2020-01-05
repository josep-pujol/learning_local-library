from django.urls import path
from . import views

urlpatterns = [
    # Function view
    path('', views.index, name='index'),
    # Class view
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]
