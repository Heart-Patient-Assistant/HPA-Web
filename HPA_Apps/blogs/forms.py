from django import forms
from .models import Post, Category, Comment

# to hard code choices
# choices = [('sport','sport'),('cars','cars'),('Big Choice','Big Choice')]
choices = Category.objects.all().values_list("name", "name")
choices_list = []
for item in choices:
    choices_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "category", "author", "body", "header_image")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            # "author": forms.Select(attrs={"class": "form-control", "readonly": True}),
            # "author": forms.TextInput(attrs={"readonly": True,),
            "author": forms.HiddenInput(),
            "category": forms.Select(
                choices=choices_list, attrs={"class": "form-control"}
            ),
            "body": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "cols": 15}
            ),
        }

    # def __init__(self, *args, **kwargs):
    #     self.user: Account = kwargs.pop("user", None)
    #     super(PostForm, self).__init__(*args, **kwargs)

    # def save(self, commit=True):
    #     post = super().save(commit=False)
    #     if commit:
    #         post.author = self.user
    #         post.save()
    #     return post


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.HiddenInput(),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author", "body")

        widgets = {
            # "author": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.HiddenInput(),
            "body": forms.Textarea(
                attrs={"class": "form-control", "rows": 2, "cols": 10}
            ),
        }
