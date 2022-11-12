from rest_framework import generics, status
from rest_framework.response import Response

from .models import Article, Author
from .serializers import ArticleSerializer


class ArticleQueryMixin:

    request = None

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Article.objects.filter(author__user=self.request.user)
        return False


class CreateArticleAPIView(generics.CreateAPIView):
    serializer_class = ArticleSerializer


class ListArticleAPIView(ArticleQueryMixin, generics.ListAPIView):
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        if self.get_queryset() is False:
            return Response(
                data={"message": "Not Allowed"}, status=status.HTTP_403_FORBIDDEN
            )
        return super().list(request, *args, **kwargs)


class DetailArticleAPIView(ArticleQueryMixin, generics.RetrieveAPIView):
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        if self.get_queryset() is False:
            return Response(
                data={"message": "Not Allowed"}, status=status.HTTP_403_FORBIDDEN
            )
        return super().get(request, *args, **kwargs)


class UpdateArticleAPIView(ArticleQueryMixin, generics.UpdateAPIView):
    serializer_class = ArticleSerializer

    def update(self, request, *args, **kwargs):
        if self.get_queryset() is False:
            return Response(
                data={"message": "Not Allowed"}, status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)


class DeleteArticleAPIView(ArticleQueryMixin, generics.DestroyAPIView):
    serializer_class = ArticleSerializer

    def delete(self, request, *args, **kwargs):
        if self.get_queryset() is False:
            return Response(
                data={"message": "Not Allowed"}, status=status.HTTP_403_FORBIDDEN
            )
        return super().delete(request, *args, **kwargs)
