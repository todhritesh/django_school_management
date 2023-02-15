from django.db import models

GENDER = (
    ("Male","Male"),
    ("Female","Female"),
    ("Others","Others"),
)

NATIONALITY = (
    ("Indian","Indian"),
    ("Other","Other"),
)

CLASSNAME = (
    ("LKG","LKG"),
    ("UKG","UKG"),
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10"),
    ("11","11"),
    ("12","12"),
)

class Class(models.Model):
    name = models.CharField(max_length=3,choices=CLASSNAME)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    full_name = models.CharField( max_length=200)
    father_name = models.CharField( max_length=200)
    mother_name = models.CharField( max_length=200)
    address = models.CharField( max_length=200)
    city = models.CharField( max_length=200)
    state = models.CharField( max_length=200)
    pin_code = models.CharField( max_length=200)
    nationality = models.CharField( max_length=200 , choices=NATIONALITY)
    contact = models.CharField( max_length=200)
    image = models.ImageField(upload_to='students/',null=True,blank=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10,choices=GENDER)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
    
    