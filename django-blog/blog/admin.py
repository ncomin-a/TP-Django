from django.contrib import admin
from blog.models import Category, Comment, Post


class CategoryAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_on")
    list_filter = ("categories",)
    search_fields = ("title", "body")


class CommentAdmin(admin.ModelAdmin):
    # Solo el administrador puede eliminar comentarios (desde /admin/)
    list_display = ("author", "post", "created_on")
    list_filter = ("post",)
    search_fields = ("author", "body")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
