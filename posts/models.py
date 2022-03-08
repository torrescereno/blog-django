from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce import models as tinymce_models


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField()

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey('Post', related_name='comments' , on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    content = tinymce_models.HTMLField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(blank=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    def view_count(self):
        return PostView.objects.filter(post=self).count()

