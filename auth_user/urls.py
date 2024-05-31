from django.urls import path
from auth_user.views import *


urlpatterns = [
    path('verifications/', VerificstionEmail.as_view(), name='verification'),
    path('signup/', Signup.as_view(), name='signup'),
    path('signin/', Signin.as_view(), name='signin'),
    path('forgot/', ForgotPassword.as_view(), name='forgot'),
    path('newpassword/', NewPassword.as_view(), name='newpassword'),
]

