from io import BytesIO

from django.core.files.base import ContentFile
from django.db import models
from PIL import Image, ImageOps


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    IMAGE_MAX_DIMENSIONS = (1600, 1200)

    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="posts/images/", blank=True, null=True)
    video = models.FileField(upload_to="posts/videos/", blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def save(self, *args, **kwargs):
        if self.image:
            previous_image_name = None
            if self.pk:
                previous_image_name = type(self).objects.filter(pk=self.pk).values_list(
                    "image", flat=True
                ).first()

            if self.image.name != previous_image_name:
                self._fit_image()

        super().save(*args, **kwargs)

    def _fit_image(self):
        image_name = self.image.name
        with Image.open(self.image) as source:
            if getattr(source, "n_frames", 1) > 1:
                return

            image_format = source.format
            image = ImageOps.exif_transpose(source)
            fitted_image = ImageOps.contain(
                image,
                self.IMAGE_MAX_DIMENSIONS,
                method=Image.Resampling.LANCZOS,
            )
            if fitted_image.size == image.size:
                return

            if image_format is None:
                raise ValueError("No se pudo determinar el formato de la imagen.")

            output = BytesIO()
            save_options = {"format": image_format}
            if image_format in {"JPEG", "WEBP"}:
                save_options["quality"] = 95
            fitted_image.save(output, **save_options)

        self.image.save(image_name, ContentFile(output.getvalue()), save=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"
