from django.db import models


class Produto(models.Model):
	nome = models.CharField('Nome', max_length=100)
	preco = models.DecimalField('Preço', decimal_places=2, max_digits=7)
	estoque = models.IntegerField('Quantidade em Estoque')
	
	
class Cliente(models.Model):
	nome = models.CharField('Nome', max_length=100)
	sobrenome = models.CharField('Sobrenome', max_length=100)
	telefone = models.CharField('Telefone', max_length=16)
	email = models.EmailField("E-Mail", max_length=100)
