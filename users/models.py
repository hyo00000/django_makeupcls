from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_customer(self, email, password, **extra_fields):
        extra_fields.setdefault('is_customer', True)
        extra_fields.setdefault('is_owner', False)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(email, password, **extra_fields)
    def create_owner(self, email, password, **extra_fields):
        extra_fields.setdefault('is_customer', False)
        extra_fields.setdefault('is_owner', True)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_customer', False)
        extra_fields.setdefault('is_owner', False)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GenderChoice = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    email = models.EmailField(max_length=30, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    nickname = models.CharField(max_length=12)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GenderChoice)
    is_customer = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

