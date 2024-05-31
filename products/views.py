from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from products.models import *
from products.permissions import IsSaler
from rest_framework.permissions import IsAuthenticated
from products.serializers import *



class ProductCreateList(APIView):
    permission_classes = [IsSaler]
    def get(self, req: Request):
        return Response({'data': Product.objects.all().values()})
    
    def post(self, req: Request):
        product_ser = ProductSerializers(data=req.data)

        if product_ser.is_valid():
            product = product_ser.save(author=req.user)


        img = req.FILES.getlist('imgs')
        videos = req.FILES.getlist('videos')

        for i in img:
            ProductImg.objects.create(product=product, img=i)

        for i in videos:
            ProductVideo.objects.create(product=product, video=i)


        return Response(ProductSerializers(product).data)



class ProductDetail(APIView):
    def get(self, req: Request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except:
            return Response({'msg': 'Product was not found !!!'}, status=404)
        video = ProductVideo.objects.all().filter(product=product)
        img = ProductImg.objects.all().filter(product=product)
        try:
            discount = Discount.objects.get(product=product).discount * (product.price / 100)
            new_price = product.price - discount
        except:
            new_price = product.price

        return Response({
             'product': ProductSerializers(product).data, 
             'new price': new_price,
             'videos': ProductVideoSerializers(video, many=True).data,
             'img': ProductImgSerializers(img, many=True).data,
            })
    
    def delete(self, req: Request, pk):
        product = Product.objects.get(pk=pk)
        if not product.author.pk == req.user.pk:
            return Response({'Error': 'Permissions error'})
        if not product.author.pk == req.user.pk:
            return Response({'Error': 'Permissions error'})
        product.delete()

        return Response({'Deleted': True})
    
    
    def post(self, req: Request, pk):
        product = Product.objects.get(pk=pk)
        if not product.author.pk == req.user.pk:
            return Response({'Error': 'Permissions error'})
        discount = req.data.get('discount')
        finish = req.data.get('finish')       

        discount_for_product = Discount.objects.create(product=product, discount=discount, finish_at=finish)

        return Response(DiscountSerializers(discount_for_product).data)
    

class ListOrder(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req: Request):
        orders = Order.objects.all().filter(custumer=req.user)

        return Response({'data': orders.values()})
    
    
class CreatetOrder(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, req: Request, pk):
        product = Product.objects.get(pk=pk)
        district = req.data.get('district')
        product_count = req.data.get('count')
        order = Order.objects.create(custumer=req.user, district=district, product=product, product_count=product_count)
        cashback = CashbackHistory.objects.get(owner=req.user)
        if product.count < int(product_count):
            return Response({"error": "Not enough products"})
        product.count -= int(product_count)
        product.save()
        cashback.total += int(product_count) * float(product.price)
        cashback.save()


        return Response({'msg': 'OK'})