from django.urls import path
from .views import ProdutoDetail, CategoriaDetail, SubCategoriaDetail


urlpatterns = [
    path('produto/<int:pk>', view=ProdutoDetail.as_view(), name='produto-detail'),
    path('categoria/<int:pk>', view=CategoriaDetail.as_view(), name='categoria-detail'),
    path('subcategoria/<int:pk>', view=SubCategoriaDetail.as_view(), name='subcategoria-detail')
]