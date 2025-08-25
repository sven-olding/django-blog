from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentBoundField(forms.BoundField):
    comment_class = "comment"

    def css_classes(self, extra_classes=None):
        classes = super().css_classes(extra_classes)
        if self.comment_class not in classes:
            classes += f" {self.comment_class}"
        return classes.strip()


class CommentForm(forms.ModelForm):
    bound_field_class = CommentBoundField

    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Your email"}),
            "body": forms.Textarea(attrs={"placeholder": "Your comment"}),
        }
