from django.urls import path
from .views import ListArticleAPIView, DetailArticleAPIView, CreateArticleAPIView, UpdateArticleAPIView, DeleteArticleAPIView


urlpatterns = [
    path("articles/create/", CreateArticleAPIView.as_view(), name="creat-article"),
    path("articles/", ListArticleAPIView.as_view(), name="list-articles"),
    path("articles/<int:pk>", DetailArticleAPIView.as_view(), name="detail-article"),
    path("articles/update/<int:pk>", UpdateArticleAPIView.as_view(), name="update-article"),
    path("articles/delete/<int:pk>", DeleteArticleAPIView.as_view(), name="delete-article"),
]
