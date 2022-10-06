from django.test import TestCase
from .models import Article

from django.utils.text import slugify

# Create your tests here.


class ArticleTestCase(TestCase):
    def setUp(self):
        self.number_of_articles = 50
        for _ in range(0, self.number_of_articles):
            Article.objects.create(title="Hello World", content="Some content")

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.number_of_articles)

    def test_hello_world_slug(self):
        obj = Article.objects.all().order_by("id").first()
        slugified_title = slugify(obj.title)
        self.assertEqual(obj.slug, slugified_title)

    def test_hello_world_id_slug(self):
        obj = Article.objects.all().get(id=2)
        self.assertEqual(obj.slug, "hello-world-2")

    def test_hello_world_uniqe_slug(self):
        qs = Article.objects.all().exclude(slug__iexact="hello-world")
        for obj in qs:
            slugified_title = slugify(obj.title)
            self.assertNotEqual(obj.slug, slugified_title)

    def test_article_search_manager(self):
        qs = Article.objects.search(query="Hello World")
        self.assertEqual(qs.count(), self.number_of_articles)
        qs = Article.objects.search(query="world")
        self.assertEqual(qs.count(), self.number_of_articles)
        qs = Article.objects.search(query="some content")
        self.assertEqual(qs.count(), self.number_of_articles)
