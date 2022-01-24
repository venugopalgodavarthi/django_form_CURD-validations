from django import forms

def firstupper(value):
    if not(value[0].isupper()):
        raise forms.ValidationError("cname first character should be upper case")

def max15(value):
    if len(value)>15:
            raise forms.ValidationError("customer name should max 15 characters ")
def min5(value):
    if len(value)<5:
            raise forms.ValidationError("customer name should min 5 characters ")
        
def finddg(st):
        for i in st:
            if i in '1234567890':
                return True
        else:
            return False
        
def findsp(st):
        for i in st:
            if i in '!@#$%^&*()_-+=*/><':
                return True
        else:
            return False
def atleastonedigit(value):
    if not(finddg(value)):
        raise forms.ValidationError("password at least one digit  ")
    
def exact10(value):
    if len(str(value))!=10:
            raise forms.ValidationError('phone number should be 10 digits')
        
def startswithdigit(value):
    if not(str(value)[0] in ['5','6','7','8','9' ]):
        raise forms.ValidationError('phone number first digit should be either 5,6,7,8 and 9')
    
def atleastonesymbol(value):
    if not(findsp(value)):
        raise forms.ValidationError("password at least one special symbol like [ ! @ # $ % ^ & * ( ) _ - + = * / > < ]")
        