from django.shortcuts import render_to_response, get_object_or_404, render
from postagens.models import Postagem, Categoria, Comentario
from django.template  import RequestContext

# Create your views here.
def home(request):
    resumos   = Postagem.objects.all()
    #resumos   = resumos.filter(categoria = 6)
    return render(request, 'postagens/index.html', locals())

def slide(request):
    slide    = Postagem.objects.all()
    slide    = posts.filter(paginas__pk=6)[:3]
    
    return render(request, 'postagens/blog.html',locals())

def blog(request):
    posts    = Postagem.objects.all()
    posts    = posts.filter(paginas__pk=1)
    categorias = Categoria.objects.all()
    
    return render(request, 'postagens/blog.html',locals())

def blog_post(request,post_pk):
    post = get_object_or_404(Postagem, pk=post_pk)
    comentarios = Comentario.objects.all().filter(post__pk=post_pk)
    
    return render(request, 'postagens/single.html',locals())

def portifolio(request):
    projetos    = Postagem.objects.all()
    #projetos    = projetos.filter(categoria = 3).order_by('pk')
    return render(request, 'postagens/portfolio.html',locals())
    

#def contato(request):
#    return render(request, 'postagens/contact.html',locals())

#def contato(request):
#    if request.method == "POST":
#        form = FormContato(request.POST, request.FILES)
#        if form.is_valid():
#            contato = form.save(commit = False)
#            contato.save()
#            return render(request, 'postagens/single.html',locals())
#    else:
#        form = FormContato()
#    return render(request, 'postagens/contact.html',locals())