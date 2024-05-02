from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    liked_by = models.ManyToManyField(User, through='LikedItem', related_name='liked_items')  
    view_count = models.IntegerField(default=0)  


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'item')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followed_by = models.ManyToManyField(User, related_name='following')
    liked_items = models.ManyToManyField(Item, related_name='liked_by_users')
    
    
class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.OneToOneField(Token, on_delete=models.CASCADE)