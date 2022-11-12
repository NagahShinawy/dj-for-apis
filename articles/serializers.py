from rest_framework import serializers
from .models import Article, Author


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("id", "username", "email", "boi")


# nested objects, nested serializers
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ("id", "author", "title", "body", "created_at")  # updated_at not included


