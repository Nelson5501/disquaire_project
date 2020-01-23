from django.db import models
from django.admin import Article, Meta


class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    slug = models.SlugField(max_length=100)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Date de parution")
    categorie = models.ForeignKey(Categorie)
    
class Meta:
        verbose_name = "article"
        ordering = ['date']

    def __str__(self):
        return self.titre