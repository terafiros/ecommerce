from django.views.generic import DetailView, TemplateView
from .models import Produto, Categoria, SubCategoria
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

class ProdutoDetail(DetailView):
    model = Produto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['produtos_relacionados'] = self.object.sub_categoria.produto_set.all()[:5]
        if self.request.user.is_authenticated:
            context['carrinho'] = self.request.user.carrinho

        return context

class CategoriaDetail(DetailView):
    model = Categoria

class SubCategoriaDetail(DetailView):
    model = SubCategoria

class CarrinhoView(LoginRequiredMixin, TemplateView):
    template_name = 'produtos/carrinho.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carrinho'] = self.request.user.carrinho
        return context

@login_required
def adiciona_produto_carrinho(request, pk):
    carrinho = request.user.carrinho
    produto = get_object_or_404(Produto, pk=pk)
    carrinho.produto_set.add(produto)

    response = {
        'num_produtos':carrinho.produto_set.count(),
        'success':True
    }

    return JsonResponse(response)

