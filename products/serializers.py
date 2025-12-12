# serializers.py (o categories/serializers.py + products/serializers.py)
from rest_framework import serializers
from .models import Product, Category
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agrega datos personalizados al token
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff  # opcional

        return token

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id_category', 'name', 'description']
        read_only_fields = ['id_category']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'amount', 'category']
