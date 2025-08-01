from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Input your Email")
        
        "Convertion of the email to a standard format like lowercase"
        email = self.normalize_email(email)

        "Creation of instance of the user model"
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        "Saves the user in the database"
        user.save()

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)

"A Defined custom user model"  "(PermissionsMixin) for permissions and roles."
class User(AbstractBaseUser, PermissionsMixin): # Usage of (AbstractBaseUser) for password handling.
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=75)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)  # Bonus Task
    date_joined = models.DateTimeField(default=timezone.now)

    "Use the email field instead of the username(default) as the login"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    "Returning readable string"
    def __str__(self):
        return self.email
    
class Profile(models.Model):
    "Defined role choices"
    ROLES = (
        ('student', 'Student'),
        ('vendor', 'Vendor'),
        ('admin', 'Admin')
    )
    "Made sure one user has only one profile, also if a user is deleted, the profile is also deleted"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    "Stores a user phone no, to prevent duplicated numbers"
    phone_number = models.CharField(max_length=14, unique=True)
    role = models.CharField(max_length=10, choices=ROLES)
    "stores the user date of birth"
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.user.email} Profile"
    
