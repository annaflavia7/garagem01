from django.db import models


class Acessorios(models.Model):
    descricao = models.CharField(max_length=80, default=0)

    def __str__(self):
        return self.descricao
