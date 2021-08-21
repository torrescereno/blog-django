from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce import models as tinymce_models


# Registras cantidad de post de un user
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# Categoria
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Autor / Perfil
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField()

    def __str__(self):
        return self.user.username


# Comentario
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey('Post', related_name='comments' , on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    
# Post 
class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    content = tinymce_models.HTMLField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


    # Ruta para ir al detalle del post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    # Ruta para actulizar el post
    def get_update_url(self):
        return reverse('post-update', kwargs={'pk': self.pk})

    # Ruta para eliminar un post
    def get_delete_url(self):
        return reverse('post-delete', kwargs={'pk': self.pk})

    # Obtiene todas las propiedades
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    # Obtiene el contador de comentarios
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    # Obtiene el contador de vistas
    def view_count(self):
        return PostView.objects.filter(post=self).count()

