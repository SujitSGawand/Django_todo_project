from django.db import models
from django.urls import reverse

class ToDo(models.Model):
    titleTask = models.CharField(max_length=25)
    textTask = models.TextField()
    statusTask = models.BooleanField(default=False)
    authorTask = models.ForeignKey('auth.User', on_delete = models.CASCADE)

    def __str__(self):
        return self.titleTask
    def get_absolute_url(self):
        return reverse('home')