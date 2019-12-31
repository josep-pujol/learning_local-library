from django.urls import path
from . import views

urlpatterns = [
    # Function view
    path('', views.index, name='index'),
    # Class view
    path('books/', views.BookListView.as_view(), name='books'),
]
