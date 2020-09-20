from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import ArticleForm, MessageForm, AboutMeForm, aboutMeImagesForm
from .models import Article, Comment, Message, aboutMeImages, AboutMe
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect


def loadtrial(request):
    print("Loading articles:")
    keyword = request.GET.get("keyword")
    print("Keyword : ", keyword)
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "allarticles.html", {"articles": articles})
    articles = Article.objects.all()
    print(articles)
    return render(request, "allarticles.html", {"articles": articles})


def articles(request):
    print("Loading articles:")
    keyword = request.GET.get("keyword")
    print("Keyword : ", keyword)
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "allarticles.html", {"articles": articles})
    articles = Article.objects.all()
    print(articles)
    return render(request, "allarticles.html", {"articles": articles})

def msg(request):
    print("Loadin Messages")
    msgs = Message.objects.all()
    print(msgs)
    return render(request, "messages.html", {"msgs": msgs})

def addMessage(request):
    form = MessageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        msg = form.save(commit=False)
        msg.slug = slugify(msg.title)
        # msg.author = request.user
        msg.save()

        messages.success(request, "The message was created successfully")
        return HttpResponseRedirect("/messages")
    return render(request, "addmessage.html", {"form": form})


def index(request):
    print("Loading articles:")
    keyword = request.GET.get("keyword")
    print("Keyword : ", keyword)
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "messages.html", {"articles": articles})
    articles = Article.objects.all()
    print(articles)
    return render(request, "allarticles.html", {"articles": articles})
    # return render(request, "index.html")

def about(request):
    if request.user.is_authenticated:
        about = AboutMe.objects.filter(author=request.user).last()
        if about:
            print(about)
            imgs = aboutMeImages.objects.filter(about=about)
            print(imgs)
            return render(request, "about.html", {"about":about,"imgs":imgs})
        else:
            return HttpResponseRedirect('/addaboutme')
    # return render(request, "addaboutme.html")
    return HttpResponseRedirect("/article")


@login_required(login_url="user:login")
def addabout(request):
    ImageFormSet = modelformset_factory(aboutMeImages, form=aboutMeImagesForm, extra=10)
    print(request.user.is_authenticated)
    if request.method == 'POST':
        aboutForm = AboutMeForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=aboutMeImages.objects.none())

        if aboutForm.is_valid() and formset.is_valid():
            x = aboutForm.save(commit=False)
            x.author = request.user
            x.save()

            for y in formset.cleaned_data:
                if y:
                    img = y['image']
                    photo = aboutMeImages(about = x, image=img)
                    photo.save()
            messages.success(request, "The page was updated successfully")
            return HttpResponseRedirect("/about")
        else:
            print(aboutForm.errors, formset.errors)
    else:
        aboutmeform = AboutMeForm()
        formset = ImageFormSet(queryset=aboutMeImages.objects.none())
    return render(request, "addaboutme.html", {'postForm': aboutmeform, 'formset': formset})


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.slug = slugify(article.title)
        article.author = request.user
        article.save()

        messages.success(request, "The article was created successfully")
        return redirect("article:dashboard")
    return render(request, "addarticle.html", {"form": form})


def detail(request, slug):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.all()
    return render(request, "detail.html", {"article": article, "comments": comments})

def msgdetail(request, slug):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Message, slug=slug)
    # comments = article.comments.all()
    msgs = {
        "message" : True
    }
    return render(request, "detail.html", {"article": article, "msgs": msgs})


@login_required(login_url="user:login")
def updateArticle(request, slug):

    article = get_object_or_404(Article, slug=slug)
    form = ArticleForm(request.POST or None,
                       request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request, "Makale başarıyla güncellendi")
        return redirect("article:dashboard")

    return render(request, "update.html", {"form": form})


@login_required(login_url="user:login")
def deleteArticle(request, slug):
    article = get_object_or_404(Article, slug=slug)

    article.delete()

    messages.success(request, "Article deleted successfully")

    return redirect("article:dashboard")


def addComment(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author,
                             comment_content=comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail", kwargs={"slug": slug}))
