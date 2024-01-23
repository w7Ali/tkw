# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from django.utils import timezone
from .models import Product
from .serializers import ProductSerializer

@api_view(['POST', 'PUT'])
def add_product(request):
        serializer = ProductSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ParseError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def all_product(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # if pk is not None:
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)


    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        product.delete()
        return Response("Product Deleted Successfuly")

@api_view(['GET'])
def top_products(request, period):
    now = timezone.now()

    if period == 'all':
        products = Product.objects.order_by('-retrieval_count')[:5]
    elif period == 'last_day':
        yesterday = now - timezone.timedelta(days=1)
        products = Product.objects.filter(
            created_at__gte=yesterday
        ).order_by('-retrieval_count')[:5]
    elif period == 'last_week':
        last_week = now - timezone.timedelta(days=7)
        products = Product.objects.filter(
            created_at__gte=last_week
        ).order_by('-retrieval_count')[:5]
    else:
        return Response({'error': 'Invalid period parameter'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
