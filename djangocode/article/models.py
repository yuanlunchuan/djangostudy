from django.db import models

class Article(models.Model):
  title = models.CharField(verbose_name='文章标题', max_length=30)
  content = models.TextField(verbose_name='文字内容')

  class Meta:
    verbose_name = '文章'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.title
