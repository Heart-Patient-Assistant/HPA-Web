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
        fields = ("title", "title_tag", "author", "category", "body", "header_image")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(
                choices=choices_list, attrs={"class": "form-control"}
            ),
            "body": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "cols": 15}
            ),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "body")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(
                attrs={"class": "form-control", "rows": 2, "cols": 10}
            ),
        }
