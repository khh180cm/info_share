from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin


class UserManager(BaseUserManager):
    '''
    Provides helper function for creating a user and a superuser
    '''
    def create_user(self, email, password=None, **extra_fields):
        '''creates and saves a new user'''
        if not email or '@' not in email:
            raise ValueError('Email address needed!')

        domain_part = email.split(sep='@')[1]
        if '.' not in domain_part:
            raise ValueError('Incorrect email')
        user = self.model(
                email=self.normalize_email(email),
                **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        '''Creates a superuser'''
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    '''Custom user model that supports email rather than username'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, blank=True, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.OneToOneField(
            'Profile',
            on_delete=models.CASCADE,
            null=True
    )
    comment = models.ManyToManyField(
        'comment.Comment',
        through='comment.UserComment'
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'users'


class Profile(models.Model):
    '''Personal user profile'''
    image = models.ImageField(blank=True)
    bio = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profiles'
