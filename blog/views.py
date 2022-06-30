from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    """
    post_list: leva a solicitação e irá
    retorn: retorna o valor que recebe ao chamar outra função render
        que irá renderizar (montar) nosso modelo blog/post_list.html.
    """
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': post})
