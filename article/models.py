from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify 
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Author ")
    title = models.CharField(max_length = 50,verbose_name = "Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Created On")
    article_image = models.FileField(blank = True,null = True,verbose_name="Image", default="bg_1.jpg")
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):    
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)        

    class Meta:
        ordering = ['-created_date']

class Message(models.Model):
    # author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Author ")
    name = models.CharField(max_length=25, verbose_name="Author Name")
    title = models.CharField(max_length = 50,verbose_name = "Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Created On")
    birthday_image = models.FileField(blank = True,null = True,verbose_name="Image", default="bg_1.jpg")
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):    
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Message, self).save(*args, **kwargs)        

    class Meta:
        ordering = ['-created_date']

class AboutMe(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Author")
    title = models.CharField(max_length=50, verbose_name= "Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Created On")

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)  

class aboutMeImages(models.Model):
    about = models.ForeignKey(AboutMe,on_delete=models.CASCADE, verbose_name="About Me")
    image = models.ImageField(blank=True, null=True, verbose_name="Image", default="bg_1.jpg")

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Article",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "Author")
    comment_content = models.CharField(max_length = 200,verbose_name = "Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']