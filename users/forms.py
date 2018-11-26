from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser , JobProfile ,BankProfile ,Salary

usertypes= (
    ('1', 'Admin'),
    ('2', 'Accountant'),
    ('3', 'Staff'),
    
    )

    #
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30,required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    #usertype= forms.CharField(label='Role', widget=forms.Select(choices=usertypes))
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email','first_name','last_name')
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email','first_name','last_name','usertype')
    
class JobProfileForm(ModelForm):
    user=forms.ModelChoiceField(
        #User.objects.annotate(
    #no_reports=~Exists(Reports.objects.filter(user__eq=OuterRef('pk')))
#).filter(
    
#    no_reports=True
#)
        queryset=CustomUser.objects.filter(jobprofile=None),
        #widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = JobProfile
        fields = ['user', 'job_title', 'department']
  
class BankForm(ModelForm):
    user=forms.ModelChoiceField(
        #User.objects.annotate(
    #no_reports=~Exists(Reports.objects.filter(user__eq=OuterRef('pk')))
#).filter(
    
#    no_reports=True
#)
        queryset=CustomUser.objects.filter(bankprofile=None),
        #widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = BankProfile
        fields = ['user', 'bank_name', 'bank_ifsc','bank_accountno']
class SalaryForm(ModelForm):
    class Meta:
        model = Salary
        fields = ['user', 'hours','month']
  