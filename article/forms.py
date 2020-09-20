from django import forms
from .models import Article, Message, AboutMe, aboutMeImages


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "article_image"]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "title", "content", "birthday_image"]


class AboutMeForm(forms.ModelForm):

    class Meta:
        model = AboutMe
        fields = {"title", "content"}


class aboutMeImagesForm(forms.ModelForm):
    class Meta:
        model = aboutMeImages
        fields = {"image"}
