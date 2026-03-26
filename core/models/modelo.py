from django.db import models


class Modelo(models.Model):
    descricao = models.CharField(max_length=80, default=0)

    def __str__(self):
        return self.descricao
