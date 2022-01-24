from django import forms
from customer.validators import *


class customerform(forms.Form):
    cname=forms.CharField(validators=[firstupper,max15,min5])
    email=forms.EmailField()
    phone=forms.IntegerField(validators=[exact10,startswithdigit])
    dob=forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    li=[['Male','MALE'],['Female','FEMALE']]
    gender=forms.ChoiceField(choices=li)
    password=forms.CharField(widget=forms.PasswordInput,validators=[min5,atleastonedigit,atleastonesymbol,firstupper])
    repassword=forms.CharField(widget=forms.TextInput,validators=[min5,atleastonedigit,atleastonesymbol,firstupper])
    
    def clean(self):
        p=self.cleaned_data['password']
        pa=self.cleaned_data['repassword']
        if p != pa:
            raise forms.ValidationError('password and repassword is not same')
   
   
   
   
   
   
    
'''
    @staticmethod
    def finddg(st):
        for i in st:
            if i in '1234567890':
                return True
        else:
            return False
        
    @staticmethod
    def findsp(st):
        for i in st:
            if i in '!@#$%^&*()_-+=*/><':
                return True
        else:
            return False
    
    def clean(self):
        cname=self.cleaned_data['cname']
        if not(cname[0].isupper()):
            raise forms.ValidationError("cname first character should be upper case")
        if len(cname)<5:
            raise forms.ValidationError("customer name should min 5 characters ")
        if len(cname)>=15:
            raise forms.ValidationError("customer name should max 15 characters ")
        
        phone=self.cleaned_data['phone']
        if len(str(phone))!=10:
            raise forms.ValidationError('phone number should be 10 digits')
        if not(str(phone)[0] in ['5','6','7','8','9' ]):
            raise forms.ValidationError('phone number first digit should be either 5,6,7,8 and 9')
        
        pa=self.cleaned_data['password']
        if len(pa)<5:
            raise forms.ValidationError('password should be min 5 characters')
        if not(pa[0].isupper()):
            raise forms.ValidationError("password first character should be alphabet and upper case")
        if not(self.finddg(pa)):
            raise forms.ValidationError("password at least one digit  ")
        if not(self.findsp(pa)):
            raise forms.ValidationError("password at least one special symbol like [ ! @ # $ % ^ & * ( ) _ - + = * / > < ]")
        
        p=self.cleaned_data['repassword']
        if len(p)<5:
            raise forms.ValidationError('password should be min 5 characters')
        if not(p[0].isupper()):
            raise forms.ValidationError("password first character should be alphabet and upper case")
        if not(self.finddg(p)):
            raise forms.ValidationError("password at least one digit  ")
        if not(self.findsp(p)):
            raise forms.ValidationError("password at least one special symbol like [ ! @ # $ % ^ & * ( ) _ - + = * / > < ]")
        if p != pa:
            raise forms.ValidationError("password and repassword  not be same")
        
    

    def clean_cname(self):
        cname=self.cleaned_data['cname']
        if not(cname[0].isupper()):
            raise forms.ValidationError("cname first character should be upper case")
        if len(cname)<5:
            raise forms.ValidationError("customer name should min 5 characters ")
        if len(cname)>=15:
            raise forms.ValidationError("customer name should max 15 characters ")
        return cname
    
    def clean_phone(self):
        phone=self.cleaned_data['phone']
        if len(str(phone))!=10:
            raise forms.ValidationError('phone number should be 10 digits')
        if not(str(phone)[0] in ['5','6','7','8','9' ]):
            raise forms.ValidationError('phone number first digit should be either 5,6,7,8 and 9')
        return phone         
    
    @staticmethod
    def finddg(st):
        for i in st:
            if i in '1234567890':
                return True
        else:
            return False
        
    @staticmethod
    def findsp(st):
        for i in st:
            if i in '!@#$%^&*()_-+=*/><':
                return True
        else:
            return False
            
    def clean_password(self):
        pa=self.cleaned_data['password']
        if len(pa)<5:
            raise forms.ValidationError('password should be min 5 characters')
        if not(pa[0].isupper()):
            raise forms.ValidationError("password first character should be alphabet and upper case")
        if not(self.finddg(pa)):
            raise forms.ValidationError("password at least one digit  ")
        if not(self.findsp(pa)):
            raise forms.ValidationError("password at least one special symbol like [ ! @ # $ % ^ & * ( ) _ - + = * / > < ]")
        return pa
    
    def clean_repassword(self):
        pa=self.cleaned_data['repassword']
        p=self.cleaned_data['password']
        if len(pa)<5:
            raise forms.ValidationError('password should be min 5 characters')
        if not(pa[0].isupper()):
            raise forms.ValidationError("password first character should be alphabet and upper case")
        if not(self.finddg(pa)):
            raise forms.ValidationError("password at least one digit  ")
        if not(self.findsp(pa)):
            raise forms.ValidationError("password at least one special symbol like [ ! @ # $ % ^ & * ( ) _ - + = * / > < ]")
        if p != pa:
            raise forms.ValidationError("password and repassword  not be same")
        return pa  
    '''
                 