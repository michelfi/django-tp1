from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Product
from .serializers import ProductSerializer


@api_view(["GET", "POST"])
def product_list_create(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data) # données reçues
        if serializer.is_valid():                        # vérifier
            serializer.save()                            # enregistrer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def product_detail_update_delete(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response({"error": "Produit non trouvé"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(ProductSerializer(product).data)

    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data) # objet + nouvelles données
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)