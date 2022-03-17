from cmath import log
from django import forms
from blog.models import Post, Comment, Category
from tinymce.widgets import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):

    CHOICE = []
    try:
        for c in Category.objects.all():
            CHOICE.append((c.pk, c))
    except Exception as e:
        print(str(e))

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ingrese un titulo"}
        )
    )

    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
        choices=CHOICE,
    )

    content = forms.CharField(
        widget=TinyMCEWidget(
            mce_attrs={"content_css": "/static/css/style.css"},
            attrs={
                "required": False,
                "rows": "10",
                "placeholder": "Ingresa el contenido del post",
                "class": "",
            },
        )
    )

    thumbnail = forms.ImageField(
        required=False, widget=forms.FileInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Post
        fields = ("title", "categories", "content", "thumbnail")


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control form-control-sm",
                "id": "usercomment",
                "placeholder": "Ingresa un comentario...",
            }
        )
    )

    class Meta:
        model = Comment
        fields = ("content",)
