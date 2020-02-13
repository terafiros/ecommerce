from django.urls import path
from .views import ProdutoDetail, CategoriaDetail, SubCategoriaDetail, CarrinhoView, adiciona_produto_carrinho


urlpatterns = [
    path('produto/<int:pk>', view=ProdutoDetail.as_view(), name='produto-detail'),
    path('categoria/<int:pk>', view=CategoriaDetail.as_view(), name='categoria-detail'),
    path('subcategoria/<int:pk>', view=SubCategoriaDetail.as_view(), name='subcategoria-detail'),
    path('carrinho', view=CarrinhoView.as_view(), name='carrinho'),
    path('carrinho/adicionar/<int:pk>', view=adiciona_produto_carrinho, name='carrinho-add-produto')
]