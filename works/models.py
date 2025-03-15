from django.db import models
from ckeditor.fields import RichTextField
from tags.models import Tag


# Create your models here.

class Work(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    work_image = models.ImageField(upload_to="works/", blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('tags.Tag', related_name='works')

    class Meta:
        ordering = ['-date_posted']
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return self.title
