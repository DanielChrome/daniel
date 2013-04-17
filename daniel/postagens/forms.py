from django import forms
from models import Contato, Comentario

class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ('nome', 'email', 'telefone', 'mensagem')

class FormComentario(forms.ModelForm):
	class Meta:
		model = Comentario
		exclude = ('datacomentario','post')

def add_comentario(request, pk):
    """Add a new comment."""
    p = request.POST

    if p.has_key("comentario") and p["comentario"]:
        author = "Anônimo"
        if p["nome"]: nome = p["nome"]

        comment = Comentario(post=Postagem.objects.get(pk=pk))
        cf = CommentForm(p, instance=comment)
        cf.fields["nome"].required = False

        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("postagens.views.blog_post", args=[pk]))