from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from posts.forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin

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
    ordering = ['-created']
    #paginate_by = 3

    # Funcion para obtener todos el contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

# Obtener el detalle de un blog
class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    form = CommentForm()

    # Crear la union del post con el usuario si el user esta autenticado
    def get_object(self, *args, **kwargs):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=obj)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post-detail', kwargs={'pk': post.pk}))

class ProfileView(LoginRequiredMixin, TemplateView):
    model = Author
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["numPosts"] = PostView.objects.filter(user=self.request.user).count()
        return context

# Creacion de post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Create' 
        return context

    def form_valid(self, form):
        form.instance.author = get_author(self.request.user)
        form.save()
        return redirect(reverse('post-detail', kwargs={'pk': form.instance.pk}))

# Actulizar post
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context

    def form_valid(self, form):
        form.instance.author = get_author(self.request.user)
        form.save()
        return redirect(reverse('post-detail', kwargs={'pk': form.instance.pk}))

# Delete Post
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = ''
    template_name = 'post_confirm_delete.html'

