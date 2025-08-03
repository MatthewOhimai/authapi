# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        
        "Convertion of the email to a standard format like lowercase"
        email = self.normalize_email(email)

        "Creation of instance of the user model"
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        "Reuseing the create_user method for creating a superuser"
        return self.create_user(email, username, password, **extra_fields)

"A Defined custom user model"  "(PermissionsMixin) for permissions and roles."
class User(AbstractBaseUser, PermissionsMixin):  # Usage of (AbstractBaseUser) for password handling.
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)  # Bonus Aspect
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    "field required when creatiing superuser"
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('vendor', 'Vendor'),
        ('admin', 'Admin'),
    )
    "Making each profile been linked to only one user"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    "unique used to prevent duplicated numbers"
    phone_number = models.CharField(max_length=14, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} Profile"