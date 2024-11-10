from django.db import models
from django.contrib.auth.models import User

class PostManager(models.Manager):
    def published(self):
        return self.filter(published_date__isnull=False)

    def by_author(self, author):
        return self.filter(author=author)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)

    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    objects = PostManager()

    def __str__(self):
        return "Title: {self.title}, content: {self.content}, author: {author}, published_date: {published_date}"
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
