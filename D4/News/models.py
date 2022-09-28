from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.validators import MinValueValidator
from django.urls import reverse

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating_pt'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating_cm'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.rating_author = pRat * 3 + cRat
        self.save()
    def __str__(self):
        return f'{self.authorUser.username.title()}'

class Category(models.Model):
    name_category = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.name_category}'

class Post(models.Model):

    ARTICLE = 'AR'
    NEWS = 'NW'
    CHANGE = [
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')

    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    change = models.CharField(max_length=2, choices=CHANGE, default=ARTICLE)
    some_data = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    content = models.TextField()
    rating_pt = models.SmallIntegerField(default=0)


    def like(self):
         self.rating_pt += 1
         self.save()

    def dislike(self):
         self.rating_pt -= 1
         self.save()

    def preview(self):
        return self.content[0:123] + '...'

    def __str__(self):
        return self.title.title()







    def get_absolute_url(self):
        return reverse('News')



class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.postThrough}:{self.categoryThrough}'

class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    some_data_cm = models.DateTimeField(auto_now_add= True)
    rating_cm = models.SmallIntegerField(default=0)

    def like(self):
        self.rating_cm += 1
        self.save()

    def dislike(self):
        self.rating_cm -= 1
        self.save()
    def __str__(self):
        return self.text
