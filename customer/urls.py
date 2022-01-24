from django.urls import path
from customer import views
app_name='customer'
urlpatterns=[
    path('cregister/',views.customerreg,name='cregister'),
    path('cselect/',views.cselect,name='cselect'),
    path('cupdate/<data>/',views.cupdate,name='cupdate'),
    path('cdelete/<data>/',views.cdelete,name='cdelete'),
    ]