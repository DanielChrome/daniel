from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Categoria(models.Model):
    nome = models.CharField(max_length = 255)
    
    def __unicode__(self):
    	return "%s" % (self.nome)

class Pagina(models.Model):
    nome = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return "%s" % (self.nome)

class Postagem(models.Model):
    titulo         = models.CharField(max_length = 255)
    datapublicacao = models.DateField()
    usuario        = models.ForeignKey(User)
    conteudo       = models.TextField()
    categoria      = models.ForeignKey(Categoria)
    paginas        = models.ManyToManyField(Pagina)
    imagem         = models.ImageField(upload_to = 'blog_posts/', null=True, blank=True)

    def __unicode__(self):
    	return "%s - %s" % (self.titulo, self.categoria.nome)
