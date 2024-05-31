from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from auth_user.models import *
from auth_user.utlis import send_password_email, send_verification_email
from django.core import signing
from rest_framework_simplejwt.tokens import RefreshToken
from products.models import CashbackHistory



class Signup(APIView):
    def get(self, req: Request):
        return Response({'msg': 'Signup'})
    
    def post(self, req: Request):
        username = req.data.get('username')
        email = req.data.get('email')
        password = req.data.get('password')
        phone = req.data.get('phone')
        is_saler = req.data.get('is_saler') == 'yes'

        user = User.objects.create_user(username=username, email=email, password=password, phone=phone)

        if is_saler:
            user.is_saler = True
            user.save()

        send_verification_email(user)

        return Response({'msg': 'OK'})
    

class VerificstionEmail(APIView):
    def get(self, req: Request):
        t = req.query_params.get('token')

        try :
            token = signing.loads(t, max_age=300)
        except:
            return Response({'error': 'Token is not actualy'})

        user = User.objects.get(pk=token)

        user.email_verification = True
        user.is_active = True

        user.save()

        tokens = RefreshToken.for_user(user)

        cashback = CashbackHistory.objects.create(owner=user)

        return Response({
            'access_token': str(tokens.access_token),
            'refresh_token': str(tokens)
        })
    

class Signin(APIView):
    def get(self, req: Request):
        return Response({'msg': 'Signin'})
    
    def post(self, req: Request):
        username = req.data.get('username')
        password = req.data.get('password')

        user = User.objects.get(username=username)

        if not user.check_password(password):
            return Response({'error': 'Wrong password !!!'})
        
        tokens = RefreshToken.for_user(user)

        return Response({
            'access_token': str(tokens.access_token),
            'refresh_token': str(tokens)
        })
    


class ForgotPassword(APIView):
    def post(self, req: Request):
        username = req.data.get('username')

        user = User.objects.get(username=username)

        send_password_email(user)

        return Response({'msg': 'Check your email'})

class NewPassword(APIView):
    def post(self, req: Request):
        t = req.query_params.get('token')

        try :
            token = signing.loads(t, max_age=300)
        except:
            return Response({'error': 'Token is not actualy'})

        user = User.objects.get(pk=token)

        p = str(req.data.get('new'))

        user.set_password(raw_password=p)

        user.save()

        return Response({'msg': 'New password'})
    