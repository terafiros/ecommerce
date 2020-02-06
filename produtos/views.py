from django.views.generic import DetailView
from .models import Produto, Categoria, SubCategoria

class ProdutoDetail(DetailView):
    model = Produto

class CategoriaDetail(DetailView):
    model = Categoria

class SubCategoriaDetail(DetailView):
    model = SubCategoria

