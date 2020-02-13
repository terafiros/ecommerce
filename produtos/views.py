from django.views.generic import DetailView, TemplateView, ListView
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

        context['no_carrinho'] = True if self.object in self.request.user.carrinho.produto_set.all() else False

        return context

class CategoriaDetail(DetailView):
    model = Categoria

class SubCategoriaDetail(DetailView):
    model = SubCategoria

class CarrinhoView(LoginRequiredMixin, ListView):
    template_name = 'produtos/carrinho.html'
    login_url = reverse_lazy('login')
    context_object_name = 'carrinho'

    def get_queryset(self):
        return self.request.user.carrinho.produto_set.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = self.request.user.carrinho.total()

        return context

@login_required
def adiciona_produto_carrinho(request, pk):
    carrinho = request.user.carrinho
    produto = get_object_or_404(Produto, pk=pk)
    carrinho.produto_set.add(produto)

    response = {
        'num_produtos':carrinho.produto_set.count(),
        'no_carrinho': True,
    }

    return JsonResponse(response)

@login_required
def remove_produto_carrinho(request, pk):
    carrinho = request.user.carrinho
    produto = get_object_or_404(Produto, pk=pk)
    carrinho.produto_set.remove(produto)

    response = {
        'num_produtos':carrinho.produto_set.count(),
        'no_carrinho':False,
        'id_removido':'#' + str(pk),
        'total':carrinho.total()
    }

    return JsonResponse(response)

