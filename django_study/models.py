from django.db  import models 


class Pessoa (models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    
    
    def __str__(self):
        return self.name
    