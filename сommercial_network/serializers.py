from rest_framework import serializers

from .models import Company, Product, Network


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkSerializer(serializers.ModelSerializer):
    companies = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Network
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    network = NetworkSerializer(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ['debt']
        depth = 1
