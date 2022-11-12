from django.contrib import admin
from .models import Author, Article


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "boi")
    list_display_links = ("id", "username")


@admin.register(Article)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "body", "created_at")
    list_display_links = ("id", "title")
