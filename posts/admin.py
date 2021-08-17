from django.contrib import admin
from posts.models import Author, Category, Post, Comment, PostView


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'overview', 'content', 'author', 'thumbnail', 'get_categories')
    readonly_fields = ('created', )

    @staticmethod
    def get_categories(self, obj):
        return "\n".join([c.categories for c in obj.categories.all()])


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'content', 'post')


@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')