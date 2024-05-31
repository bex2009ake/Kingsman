from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.



class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username or not email:
            raise ValueError('Username or email is wrong !!!')
        
        email = self.normalize_email(email=email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(username=username, email=email, password=password, **extra_fields)
    


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_saler = models.BooleanField(default=False)
    email_verification = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

    objects = UserManager()


    def __str__(self) -> str:
        return self.username
