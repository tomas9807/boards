from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=20,help_text='name of the board',unique=True)
    description = models.TextField()
    def __str__(self):
        return f'{self.name}'

class Topic(models.Model):
    board_belongs = models.ForeignKey(Board,on_delete=models.CASCADE,related_name='topics',blank=True,null=True)
    subject = models.CharField(max_length=20,help_text='the subject of the topic')
    last_update = models.DateTimeField(auto_now_add=True)
    stater = models.OneToOneField(User,on_delete=models.CASCADE,related_name='topics')
    def __str__(self):
        return f'{self.subject}'

class Post(models.Model):
    topic_belongs = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='topic')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True,blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    updated_by = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL,related_name='+')
    def __str__(self):
        return f'post from {self.created_by}'



