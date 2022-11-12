from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .models import Article, Author
from .serializers import ArticleSerializer


class CreateArticleAPIView(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class ListArticleAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class DetailArticleAPIView(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class UpdateArticleAPIView(generics.UpdateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class DeleteArticleAPIView(generics.DestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
