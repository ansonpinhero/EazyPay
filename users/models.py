from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
usertypes= (
    ('1', 'Admin'),
    ('2', 'Accountant'),
    ('3', 'Staff'),
    
    )

    
class CustomUser(AbstractUser):
    # add additional fields in here
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    usertype = models.CharField(max_length=100, blank=True, null=True)
    usertype = models.CharField(
        max_length=2,
        choices=usertypes,
        
    )
    
    def __str__(self):
        return self.email
#class bankaccount(model.Models)