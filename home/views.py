from django.views.generic import ListView
from produtos.models import Categoria, Produto

class HomeView(ListView):
    template_name = 'home/home.html'
    model = Categoria
    context_object_name = 'categorias'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        produtos_em_promocao = Produto.objects.filter(promocao=True)
        produtos_em_destaque = Produto.objects.all().order_by('-preco')[:30]
        context['produtos_em_promocao'] = produtos_em_promocao
        context['produtos_em_destaque'] = produtos_em_destaque
        return context





