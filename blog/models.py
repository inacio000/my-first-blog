from django.conf import settings
from django.db import models
from django.utils import timezone

# models.Model significa que o Post é um modelo de Django, então o Django sabe que ele deve ser salvo no banco de dados.
# models.CharField - é assim que definimos um texto com um número limitado de caracteres.
# models.TextField - este campo é para textos sem um limite fixo. Parece ideal para o conteúdo de um blog, né?
# models.DateTimeField - este é uma data e hora.
# models.ForeignKey - este é um link para outro modelo.


class Post(models.Model):   # definindo o nosso modelo (definindo um objeto)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # link para outro modelo
    title = models.CharField(max_length=200)    # texto com numero limitado de caracteres
    text = models.TextField()   # textos sem um limite fixo
    created_date = models.DateTimeField(default=timezone.now)   # data e hora
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # quando chamarmos __str__(), obteremos um texto (string) com o título do Post.
    def __str__(self):  # __ dunder(double-underscore (sblinhado duplo))
        return self.title
