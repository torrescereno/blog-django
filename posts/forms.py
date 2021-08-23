from django import forms
from posts.models import Post, Comment, Category
from tinymce.widgets import TinyMCE

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class PostForm(forms.ModelForm):

    CHOICE = []
    for c in Category.objects.all():
        CHOICE.append((c.pk, c))

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class':'post__form__create__title',
        'placeholder':'Ingrese un titulo'
    }))

    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={
        'required': True,
        'class':'post__form__create__categories'
    }), choices=CHOICE)

    content = forms.CharField(widget=TinyMCEWidget(mce_attrs={'content_css': "/static/css/style.css"}, attrs={
        'required': False, 
        'rows': '10', 
        'placeholder': 'Ingresa el contenido del post',
        'class': 'post__form__create__content'
    }))

    thumbnail = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ('title','categories', 'content', 'thumbnail')


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'post__form__comment',
        'id': 'usercomment',
        'rows': '5',
        'style': 'resize: none',
    }))

    class Meta:
        model = Comment
        fields = ('content',)

