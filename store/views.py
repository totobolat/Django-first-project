from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, CollectionSerializer
from .models import OrderItem, Product, Collection
from django.db.models.aggregates import Count

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count > 0:
            return Response({'error': 'cant delete'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products'))
    serializer_class = CollectionSerializer

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']):
            return Response({'error': 'cant delete'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    # def delete(self, request, pk):
    #     collection = get_object_or_404(Product, pk=pk)
    #     if collection.products.count() > 0:
    #         return Response({'error': 'cant delete'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# class ProductList(ListCreateAPIView):
#     # def get(self, request):
#     #     queryset = get_queryset()
#     #     serializer = ProductSerializer(queryset, many=True)
#     #     return Response(serializer.data)
#     # def post(self, request):
#     #     serializer = ProductSerializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    

# class CollectionDetail(RetrieveUpdateDestroyAPIView):
#     # collection = get_object_or_404(Collection.objects.annotate(products_count=Count('products')), pk=id)
#     # if request.method == 'GET':
#     #     serializer = CollectionSerializer(collection)
#     #     return Response(serializer.data)
#     # elif request.method == 'PUT':
#     #     serializer = CollectionSerializer(collection, data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
#     #     return Response(serializer.data)
#     # elif request.method == 'DELETE':

# class CollectionList(ListCreateAPIView):
#     queryset = Collection.objects.annotate(products_count=Count('products')).all().order_by('id')
#     serializer_class = CollectionSerializer