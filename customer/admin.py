from django.contrib import admin
from customer.models import customermodels
# Register your models here.

class admincustomermodels(admin.ModelAdmin):
    list_display=['cname','email','phone','dob','gender','password','dor']
    
admin.site.register(customermodels,admincustomermodels)