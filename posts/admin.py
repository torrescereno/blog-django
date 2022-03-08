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
    list_display = ('title', 'overview', 'content', 'author', 'thumbnail', 'get_categories', 'created')
    readonly_fields = ('created', )

    @staticmethod
    def get_categories(self):
        return "\n".join([c.name for c in self.categories.all()])


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'content', 'post')

