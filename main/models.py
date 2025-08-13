from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title


class News(models.Model):
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="image/")
    desc = models.TextField()
    publish = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

