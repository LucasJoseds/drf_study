from django.db  import models 


class Pessoa (models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    email= models.CharField(max_length=255)
    data_nascimento = models.DateTimeField
    
    
    def __str__(self):
        return self.nome
    
    class Cardapio (models.Model):
        nome = models.CharField(max_length=100)
        preco = models.DecimalField
        descricao = models.CharField(max_length=255)
        
    def __str__(self):
        return self.nome
        
         
    