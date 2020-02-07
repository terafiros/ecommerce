from random import random, randint
import django
from django.conf import settings
from django.core.exceptions import ValidationError



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'produtos',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ecommerce_data',
        'USER': 'admin',
        'PASSWORD': 'admin@2019',
        'HOST': '',
        'PORT': '',
    }
}

settings.configure(
    INSTALLED_APPS=INSTALLED_APPS,
    DATABASES=DATABASES)
django.setup()

from produtos.models import (Produto,
                             Caracteristica,
                             Categoria,
                             SubCategoria)


def drop_all_data(tables=None):
    if tables is None:
        return

    for table in tables:
        table.objects.all().delete()
        table.objects.raw('')


def cria_dados():
    for num_cate in range(5):
        c = Categoria.objects.create(
            nome=f'CATEGORIA {num_cate + 1}'
            )
        for num_sub in range(5):
            sub = SubCategoria.objects.create(
                nome=f'SUBCATEGORIA {num_sub + 1}',
                categoria=c
                )
            for num_p in range(5):
                try:
                    p = Produto.objects.create(
                        nome=f'Produto {num_p + 1}',
                        preco=random() * 10000,
                        sub_categoria=sub,
                        categoria=c
                        )
                except ValidationError as e:
                    print(e)
                    continue

                for num_carac in range(5):
                    carac = Caracteristica.objects.create(
                        nome=f'Caracteristica {num_carac + 1}',
                        descricao=f'Essa é a Caracteristica {num_carac + 1} muito boa',
                        produto=p
                        )


def cria_produto_em_promocao():
    for num_p in range(7):
        try:
            p = Produto.objects.create(
                nome=f'Produto {num_p + 1}',
                preco=random() * 10000,
                sub_categoria=SubCategoria.objects.get(pk=randint(1, SubCategoria.objects.all().count() - 1)),
                categoria=Categoria.objects.get(pk=randint(1, Categoria.objects.all().count() - 1)),
                promocao=True,
                desconto=random() * 10000
            )
        except ValidationError as e:
            print(e)
            continue

        for num_carac in range(5):
            carac = Caracteristica.objects.create(
                nome=f'Caracteristica {num_carac + 1}',
                descricao=f'Essa é a Caracteristica {num_carac + 1} muito boa',
                produto=p
            )


if __name__ == '__main__':
    #drop_all_data([Produto, Caracteristica, Categoria, SubCategoria])
    #cria_dados()
    cria_produto_em_promocao()