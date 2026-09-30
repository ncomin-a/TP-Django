from django.test import TestCase

from blog.models import Category, Comment, Post


class BlogViewsTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Django")
        self.post = Post.objects.create(title="Hello Django", body="A post body")
        self.post.categories.add(self.category)

    def test_index_lists_posts(self):
        self.assertContains(self.client.get("/"), "Hello Django")

    def test_detail_renders_comment_form(self):
        response = self.client.get(f"/post/{self.post.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="author"')
        self.assertContains(response, 'name="body"')

    def test_detail_404_for_missing_post(self):
        self.assertEqual(self.client.get("/post/999/").status_code, 404)

    def test_comment_submission(self):
        self.client.post(f"/post/{self.post.pk}/", {"author": "Ana", "body": "Genial"})
        self.assertEqual(Comment.objects.filter(post=self.post).count(), 1)

    def test_category_exact_match(self):
        self.assertContains(self.client.get("/category/Django/"), "Hello Django")
        self.assertNotContains(self.client.get("/category/Dj/"), "Hello Django")
