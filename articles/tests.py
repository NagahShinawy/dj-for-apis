from django.test import TestCase
from .models import Author, User, Article


class ArticleTestCase(TestCase):

    USERNAME = "john"
    PASSWORD = "john@123"
    BOI = "one the best player in the world"
    TITLE = "waiting for world cup"
    BODY = "Qatar hosts fifa world cup 2022"

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username=self.USERNAME, password=self.PASSWORD
        )
        self.author = Author.objects.create(user=self.user, boi=self.BOI)
        self.article = Article.objects.create(
            title=self.TITLE,
            body=self.BODY,
            author=self.author,
        )

    def test_creat_user(self):
        self.assertEqual(User.objects.all().count(), 1)

    def test_create_author(self):
        self.assertEqual(Author.objects.all().count(), 1)

    def test_create_article(self):
        return self.assertEqual(Article.objects.all().count(), 1)

    def test_article_title(self):
        self.assertEqual(Article.objects.first().title, self.TITLE)

    def test_article_body(self):
        self.assertEqual(Article.objects.first().body, self.BODY)

    def test_article_author(self):
        self.assertEqual(Article.objects.first().author, self.author)
