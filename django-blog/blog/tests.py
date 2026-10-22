from io import BytesIO
from tempfile import TemporaryDirectory

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from PIL import Image

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

    def test_large_image_is_resized_without_changing_its_aspect_ratio(self):
        image_data = BytesIO()
        Image.new("RGB", (3200, 1600), color="red").save(image_data, format="PNG")

        with TemporaryDirectory() as media_root:
            with override_settings(MEDIA_ROOT=media_root):
                self.post.image = SimpleUploadedFile(
                    "landscape.png",
                    image_data.getvalue(),
                    content_type="image/png",
                )
                self.post.save()

                with Image.open(self.post.image.path) as uploaded_image:
                    self.assertEqual(uploaded_image.size, (1600, 800))
