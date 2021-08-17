from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView
from posts.forms import PostForm

# Modelos
from posts.models import Post, Author, PostView


# Obtener los autores
def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

# Listar todos los Posteos
class PostListView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    paginate_by = 1

    # Funcion para obtener todos el contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lala'] = 'prueba'
        return context
    

# Obtener el detalle de un blog
class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post_detail'
    
    # Crear la union del post con el usuario si el user esta autenticado
    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=obj)
        return obj


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context

    
# Creacion de post
class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Create' 
        return context

    def form_valid(self, form):
        form.instance.author = get_author(self.request.user)
        form.save()
        return redirect(reverse('post-detail', kwargs={'pk': form.instance.pk}))

    