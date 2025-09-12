from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
        
    def __str__(self):
        return self.title
    
    
    


# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and save a regular User with the given email, username, and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_('The Username must be set'))
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email, username, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):

    email = models.EmailField(_('email address'), unique=True)
    """Custom user model extending AbstractUser"""
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField (upload_to='profile_photos/', null=True, blank=True)


    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']  # Username is still required


    objects = CustomUserManager()
    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'