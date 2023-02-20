from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from сommercial_network.models import Company, Network, Product
from сommercial_network.permissions import IsActivePermission
from сommercial_network.serializers import CompanySerializer, NetworkSerializer, ProductSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsActivePermission]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['country']

    def create(self, request, *args, **kwargs):
        data = request.data

        new_company = Company.objects.create(
            type=data["type"],
            hierarchy=data["hierarchy"],
            name=data["name"],
            email=data["email"],
            country=data["country"],
            city=data["city"],
            street=data["street"],
            building_number=data["building_number"],
            network=Network.objects.get(id=data["network"]),
            provider=Company.objects.get_or_none(id=data["provider"])
        )

        new_company.save()

        for product in data["products"]:
            product_obj = Product.objects.get(name=product['name'])
            new_company.products.add(product_obj)

        serializer = CompanySerializer(new_company)

        return Response(serializer.data)


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsAuthenticated, IsActivePermission]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActivePermission]

