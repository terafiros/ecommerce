from django.test import TestCase
from .models import Produto
from random import random



class ProdutoTest(TestCase):

    def setUp(self):
        self.produtos = []
        for num in range(5):
            self.produtos.append(
                Produto.objects.create(
                    nome=f'Produto {num}',
                    preco=random() * 10000
                )
            )

    def test_produto_sem_campos_obrigatorios(self):
        for p in self.produtos:
            self.assertNotEqual(p.nome, None)
            self.assertNotEqual(p.preco, None)


