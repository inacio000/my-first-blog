from cgitb import text
from django import forms
from .models import Post


# Formulario do tipo "ModelForm"
class PostForm(forms.ModelForm):

    class Meta:
        model = Post    # Qual modelo devera ser usado para criar este formulario
        fields = ('title', 'text')  # Quais campos devem entrar no nosso formulario

# Tudo o que precisamos fazer agora é usar o formulário em uma "view" e mostrá-lo em um "template".
# Vamos criar um "link" para a "página", uma "URL", uma "view" e um "template".