from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Post(models.Model):
    #Este campo aguenta ate 255 caracteres
    title = models.CharField(max_length=255)
    #Este campo vai ser o texto que vamos usar na url dos nossos posts
    slug = models.SlugField(max_length=255, unique=True)
    #Este campo vai guardar o id do autor do post
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #Este campo e o corpo do nosso post
    body = models.FileField()
    #Este campo vai adicionar automaticamente a data e a hora da criação de um arquivo
    created = models.DateTimeField(auto_now_add=True)
    #Este campo vai atualizar automaticamente a data e hora do post sempre que ele for modificado
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ("-created",)
