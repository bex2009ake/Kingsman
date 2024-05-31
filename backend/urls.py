from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/', include('auth_user.urls')),
    path('api/products/', include('products.urls'))
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



# {
#     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3NDE2ODkxLCJpYXQiOjE3MTY1NTI4OTEsImp0aSI6IjFlOGZmNTA5NGNhNTRiYjI4OTA2YjQ0YzI3NDcxNDIzIiwidXNlcl9pZCI6MTR9.qah6S7wx8TG6drm4__vmjW9bAu27xvCbBUHVmtMBb_s",
#     "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzg0ODg5MSwiaWF0IjoxNzE2NTUyODkxLCJqdGkiOiI1OTU4NTJmYTQyZDI0OTAyYTM5OTU1NDA4ZDZlYTdjYyIsInVzZXJfaWQiOjE0fQ.9-J8OyFiBzcZ6ZDd_bUe3RNSFdhOeC5CCpS4nxqoBEM"
# }