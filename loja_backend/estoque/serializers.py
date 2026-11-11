from rest_framework import serializers
from decimal import Decimal

from .models import Categoria, Ferramenta


class CategoriaSerializer(serializers.ModelSerializer):
    """Serializa os dados basicos de categoria."""

    class Meta:
        model = Categoria
        fields = ["id", "nome", "descricao", "destaque"]


class FerramentaSerializer(serializers.ModelSerializer):
    """Serializa as ferramentas mostrando dados da categoria relacionada."""

    # Prices cannot be negative; free items remain valid.
    preco = serializers.DecimalField(max_digits=8, decimal_places=2, min_value=Decimal("0"))
    categoria_nome = serializers.CharField(source="categoria.nome", read_only=True)

    class Meta:
        model = Ferramenta
        fields = [
            "id",
            "categoria",
            "categoria_nome",
            "nome",
            "marca",
            "preco",
            "estoque",
            "descricao",
            "em_promocao",
            "criado_em",
            "atualizado_em",
        ]
