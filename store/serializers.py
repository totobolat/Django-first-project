from decimal import Decimal
from rest_framework import serializers
from store.models import Product, Collection
from django.db.models.aggregates import Count

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']
    #def productInCollection(self, collection:Collection):
    #   return Collection.objects.filter(id=collection.id).aggregate(Count('product'))
    #product_count = serializers.SerializerMethodField(method_name='productInCollection')
    products_count = serializers.IntegerField(read_only=True)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection']
    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

