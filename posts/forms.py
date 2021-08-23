from django import forms
from posts.models import Post, Comment
from tinymce.widgets import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 30, 'rows': 10}))

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail', 'categories')


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

