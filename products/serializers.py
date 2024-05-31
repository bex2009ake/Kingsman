from rest_framework.serializers import ModelSerializer
from products.models import *



class SizeSerializers(ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class ColorSerializers(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class AuthorSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone']

class ProductSerializers(ModelSerializer):
    color = ColorSerializers(many=True, read_only=True)
    size = SizeSerializers(many=True, read_only=True)
    author = AuthorSerializers(read_only=True)


    class Meta:
        model = Product
        fields = ['name', 'price', 'desc', 'count', 'author', 'color', 'size', 'created_at']


class ProductVideoSerializers(ModelSerializer):
    class Meta:
        model = ProductVideo
        fields = '__all__'


class ProductImgSerializers(ModelSerializer):
    class Meta:
        model = ProductImg
        fields = '__all__'


class DiscountSerializers(ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class OrderSerializers(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'