from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionManager, PermissionsMixin

from django.utils.translation import gettext_lazy as lazyT

import uuid, random, os, string, segno
# Create your models here.

def accNo():
    accno = [random.choice(string.digits) for i in range(8)]

    return f"{random.randint(1,9)}"+"".join(accno)


class CustomUserManager(BaseUserManager):
    
    def create_user(self,email, password,**extrafields):
        if not email:
            raise ValueError(lazyT("Email must be set"))
        if not password:
            raise ValueError(lazyT("Password must be set"))
        
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extrafields)
        user.set_password(password)
        user.save()
        return user
    
        
    def create_superuser(self, email, password, **extra_fields):
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        # if extra_fields.get("is_staff") is not True:
        #     raise ValueError(lazyT("Superuser must have is_staff=True."))
        # if extra_fields.get("is_superuser") is not True:
        #     raise ValueError(lazyT("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLES = (
        ('ADMIN','admin'),
        ('TUTOR','tutor'),
        ('USER', 'user')
    )
    GENDER = (
        ("MALE", "male"),
        ("FEMALE", "female"),
        ("CUSTOM", "custom")
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="ID", editable=False)
    role = models.CharField(choices=ROLES,max_length=30)

    first_name = models.CharField(max_length=150, verbose_name="First Name")
    last_name = models.CharField(max_length=150, verbose_name="Last Name")
    gender = models.CharField(choices=GENDER, verbose_name="Gender", max_length=20)
    dob = models.DateField(verbose_name='Date of Birth', default='2000-01-01')
    email = models.EmailField(unique=True, verbose_name="Email")
    phoneNo = models.CharField(verbose_name="Phone Number", max_length=20)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def isAdmin(self):
        return self.role == "admin"
    

    def isUser(self):
        return self.role == 'user'
    


class Account(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_no = models.CharField(default=accNo(), unique=True, max_length=9, editable=False)
    balance = models.PositiveIntegerField()

    tpin = models.CharField(max_length=6)

    def __str__(self):
        return self.account_no
    
    def hashedTpin(self):
        pass

    def qrcode(self):
        details = {
            'Name': f'{self.user.first_name} {self.user.last_name}',
            'AccNo': f'{self.account_no}',
            'PhoneNo': f'{self.user.phoneNo}',
        }
        name = f"{self.account_no}.png"
        if not os.path.exists('/media/account_qr/{}'.format(name)):
            return segno.make_qr(" ".join(details.values())).save(name, scale=10)
    
    #TODO check if this works

    @staticmethod
    def get_qr_url(obj):
        if obj.image and hasattr(obj.image, 'url'):
            return obj.image.url
        else:
            return '/media/account_qr/' 