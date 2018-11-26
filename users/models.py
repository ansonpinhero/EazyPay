from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils import timezone
from decimal import *

from django.contrib.auth.models import User
from datetime import date
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator

usertypes= (
    ('1', 'Admin'),
    ('2', 'Accountant'),
    ('3', 'Staff'),
    
    )
JOB_CODES = (
                ('P1','Professor'),
                ('P2','Associate Professor'),
                ('P3','Assistant Professor'),
                ('L1','Lab Assistant'),
            )
MONTH=(
        ('1','Januvary'),
        ('2','Februvary'),
        ('3','March'),
        ('4','April'),
        ('5','May'),
        ('6','June'),
        ('7','July'),
        ('8','August'),
        ('9','September'),
        ('10','October'),
        ('11','November'),
        ('12','December'),
        
      )
    
class CustomUser(AbstractUser):
    
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    
    usertype = models.CharField(
        max_length=2,
        choices=usertypes,
    )
    
    def __str__(self):
        full_name = str(self.first_name + " " +self.last_name)
        return full_name
class BankProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
        unique=True
    )
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    bank_ifsc = models.CharField(max_length=100, blank=True, null=True)
    bank_accountno = models.CharField(max_length=100, blank=True, null=True)
    
class Salary(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='',related_name='relatedusers')
    amount= models.DecimalField(max_digits=10,decimal_places=5)
    hours=models.IntegerField(default=0)
    pay_grade = models.CharField(max_length=5,choices=JOB_CODES,default='')
    created_date = models.DateTimeField(default=timezone.now)
    month= models.CharField(max_length=5,choices=MONTH,default='')

class UserProfile(models.Model):
    COUNTRY_CODES = (
        ('+91', 'India(+91)'),
        ('+1', 'USA(+1)'),
    )

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
        unique=True
    )
    dob = models.DateField(default=date.today)
    phone_code = models.CharField(
        max_length=3,
        choices=COUNTRY_CODES,
        blank=True
    )
    # we're using in-built Regex Validator
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits number.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, default=0)  # validators should be a list
    street1 = models.CharField(max_length=5, blank=True, default='')  # validators=[street_validator],
    street2 = models.CharField(max_length=50, blank=True, default='')
    city = models.CharField(max_length=50, blank=True, default='')
    state = models.CharField(max_length=50, blank=True, default='')
    pincode_regex = RegexValidator(regex=r'^\d{6}$', message="PINCODE must be 6 digits number.")
    pincode = models.CharField(validators=[pincode_regex], blank=True, max_length=6, default='')

    def __str__(self):
        """
        It decides what to display when access objects from console
        """
        return "%s" % self.user.username

class JobProfile(models.Model):
    JOB_CODES = (
                ('P1','Professor'),
                ('P2','Associate Professor'),
                ('P3','Assistant Professor'),
                ('L1','Lab Assistant'),
            )
    DEP_CODES = (
                ('CSE','Computer Science and Engineering '),
                ('ME','Mechanical Engineering'),
                ('ECE','Electronics & Communication Engineering'),
                ('EEE','Electrical & Electronics Engineering'),
                ('CE','Civil Engineering'),
                ('AE','Automobile Engineering'),
                ('BSH','Basic Science and Humanities'),
            )
    user = models.OneToOneField(
                CustomUser,
                on_delete=models.CASCADE,
                primary_key=True,
                
            )
    identify= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='relatedjobs')
    job_title = models.CharField(
                max_length=4,
                choices=JOB_CODES,
                blank=True
            )
    
    department = models.CharField(
                max_length=4,
                choices=DEP_CODES,
                blank=True
            )

