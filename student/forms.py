from django import forms


class registerForm(forms.Form):
    
    name=forms.CharField()
    name1=forms.CharField(widget=forms.TextInput)
    address=forms.CharField(widget=forms.Textarea)
    address1=forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email=forms.EmailField()
    website=forms.URLField()
    uuid=forms.UUIDField()
    ipaddress=forms.GenericIPAddressField()
    agree=forms.BooleanField()
    notagree=forms.NullBooleanField()
    date=forms.DateField()
    date1=forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    li=['2019','2020','2021','2022']
    date2=forms.DateField(widget=forms.SelectDateWidget(years=li))
    time=forms.TimeField()
    time1=forms.CharField(widget=forms.TimeInput)
    datetime=forms.DateTimeField()
    
    phone=forms.IntegerField()
    age=forms.FloatField()
    timeduration=forms.DurationField()
    phone1=forms.DecimalField()
    p1=forms.SplitDateTimeField()
    
    images=forms.ImageField()
    file=forms.FileField()
    #file1=forms.FilePathField(path="/student/templates/")
    com=forms.ComboField(fields=[ forms.CharField(),forms.EmailField()])
    multi=forms.MultiValueField(fields=[ forms.CharField(),forms.EmailField()])
    ti=[['male','male'],['female','female']]
    gender=forms.ChoiceField(choices=ti)
    gender1=forms.ChoiceField(widget=forms.RadioSelect, choices=ti)
    gender2=forms.TypedChoiceField(choices=ti)
    tu=[['red','red'],['green','green'],['orange','orange']]
    color=forms.MultipleChoiceField(choices=tu)
    color2=forms.ChoiceField(widget=forms.CheckboxSelectMultiple(),choices=tu)
    