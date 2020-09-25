from django.db import models
from django.conf import settings


class Practices(models.Model):
  title = models.CharField(max_length=100) 
  slug = models.SlugField()
  body = models.TextField()
  thumb = models.ImageField(default='default.png', blank=True)
  u_rl = models.CharField(max_length=255,blank=True)


  def snippet(self):
    return self.body[:20]+'...'

  def __str__(self):
      return self.title
  