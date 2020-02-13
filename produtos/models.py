from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.shortcuts import reverse


class Categoria(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    descricao = models.CharField(max_length=200, blank=False, null=False, default='Venha conferir nossos produtos')

    def get_absolute_url(self):
        return reverse('categoria-detail', args=[str(self.id)])

    def __str__(self):
        return self.nome

class SubCategoria(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    descricao = models.CharField(max_length=200, blank=False, null=False, default='Dê uma olhada também')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False, null=False)

    def get_absolute_url(self):
        return reverse('subcategoria-detail', args=[str(self.id)])

class CarrinhoCompras(models.Model):

    def total(self):
        return self.produto_set.all().aggregate(preco_total=Sum('preco') - Sum('desconto'))['preco_total']

class Produto(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    preco = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False, validators=[MinValueValidator(limit_value=0)])
    codigo_barras = models.CharField(max_length=30, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    marca = models.CharField(max_length=30, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE, blank=True, null=True)

    promocao = models.BooleanField(blank=True, null=True, default=False)
    desconto = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=0,
                                   validators=[MinValueValidator(limit_value=0)])
    carrinho = models.ForeignKey(CarrinhoCompras, on_delete=models.CASCADE, blank=True, null=True)

    imagem = models.ImageField(upload_to='produtos/imagens', blank=True, null=True, default='produtos/imagens/produto.png')

    def preco_promocao(self):
        return self.preco - self.desconto

    def clean(self):
        if self.promocao and self.desconto == 0:
            raise ValidationError(
                'valor do desconto invalido, deve ser maior que zero',
                params={'desconto': self.desconto},
            )

        if not self.promocao and self.desconto > 0:
            self.desconto = 0


        if self.desconto > self.preco:
            raise ValidationError(
                'valor do desconto invalido, deve ser menor que o preço',
                params={'desconto': self.desconto,
                        'preço': self.preco,
                        },
            )


    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('produto-detail', args=[str(self.id)])

class Caracteristica(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    descricao = models.TextField(blank=False, null=False)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, blank=False, null=False)

