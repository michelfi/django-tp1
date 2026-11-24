from rest_framework import serializers
from ..models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product                                  
        fields = ["id", "name", "description", "price", "stock"] 
        read_only_fields = ["id"]

    def validate_price(self, value):
        cleaned_value = value

        if cleaned_value <= 0:
            raise serializers.ValidationError("Le prix ne peut être négatif." )

        return cleaned_value


    def validate_stock(self, value):
        cleaned_value = value

        if cleaned_value < 0:
            raise serializers.ValidationError("Le stock ne peut être négatif." )

        return cleaned_value