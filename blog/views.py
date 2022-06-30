from django.shortcuts import render


def post_list(request):
    """
    post_list: leva a solicitação e irá
    retorn: retorna o valor que recebe ao chamar outra função render
        que irá renderizar (montar) nosso modelo blog/post_list.html.
    """
    return render(request, 'blog/post_list.html', {})
