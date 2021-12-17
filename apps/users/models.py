# import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .model_managers import CustomUserManager


class User(AbstractUser):
    # pkid = models.BigAutoField(primary_key=True, editable=False)
    # id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # username = models.CharField(db_index=True, max_length=255, unique=True)
    username = None
    email = models.EmailField(_("email address"), db_index=True, unique=True)
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)

    # date_joined = models.DateTimeField(default=timezone.now)

    """USERNAME FIELD is the name of the field on the user 
    model that is used as the unique identifier"""
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # class Meta:
    #     verbose_name = _("User")
    #     verbose_name_plural = _("Users")

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    # def get_short_name(self):
    #     return self.username
    
    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip().title()
