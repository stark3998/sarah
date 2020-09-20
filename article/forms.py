from django import forms
from .models import Article, Message


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "article_image"]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "title", "content", "birthday_image"]
