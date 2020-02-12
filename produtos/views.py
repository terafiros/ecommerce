from django.views.generic import DetailView
from .models import Produto, Categoria, SubCategoria

class ProdutoDetail(DetailView):
    model = Produto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['produtos_relacionados'] = self.object.sub_categoria.produto_set.all()[:5]

        return context

class CategoriaDetail(DetailView):
    model = Categoria

class SubCategoriaDetail(DetailView):
    model = SubCategoria

