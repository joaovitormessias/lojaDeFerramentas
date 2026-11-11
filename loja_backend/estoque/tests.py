from django.test import TestCase
from .models import Categoria
from .serializers import FerramentaSerializer


class PriceValidationTests(TestCase):
    def test_negative_price_rejected_and_zero_accepted(self):
        category = Categoria.objects.create(nome='Demo')
        data = {'categoria': category.pk, 'nome': 'Tool', 'marca': 'Demo', 'preco': '-1.00', 'estoque': 0}
        serializer = FerramentaSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        data['preco'] = '0.00'
        serializer = FerramentaSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
