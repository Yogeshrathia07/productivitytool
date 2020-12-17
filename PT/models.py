from django.db import models
from django.contrib.auth.models import User

DAY_CHOICES = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),

)

class MONDAY(models.Model):
    #name = models.OneToOneField(User,on_delete=CASCADE)
    #name = models.ForeignKey(User,on_delete=CASCADE)
    subject = models.CharField(max_length=100)
    #day = models.CharField(choices=DAY_CHOICES,max_length=(20))
    starttime = models.TimeField(null=True,blank=True)
    endtime = models.TimeField(null=True,blank=True)
    #notes = models.TextField( blank=True, null=True)
    #link = models.URLField(max_length=200,blank=True,null=True)
    #def __str__(self):
    #    return self.name
class TUESDAY(models.Model):
    subject = models.CharField(max_length=100)
    starttime = models.TimeField(null=True,blank=True)
    endtime = models.TimeField(null=True,blank=True)
class WEDNESDAY(models.Model):
    subject = models.CharField(max_length=100)
    starttime = models.TimeField(null=True,blank=True)
    endtime = models.TimeField(null=True,blank=True)
class THURSDAY(models.Model):
    subject = models.CharField(max_length=100)
    starttime = models.TimeField(null=True,blank=True)
    endtime = models.TimeField(null=True,blank=True)
class FRIDAY(models.Model):
    subject = models.CharField(max_length=100)
    starttime = models.TimeField(null=True,blank=True)
    endtime = models.TimeField(null=True,blank=True)
class SATURDAY(models.Model):
    subject = models.CharField(max_length=100)
    starttime = models.TimeField(null=True,blank=True)
    endtime = models.TimeField(null=True,blank=True)
class SUNDAY(models.Model):
    subject = models.CharField(max_length=100)
    starttime = models.TimeField(null=True,blank=True)
    endtime = models.TimeField(null=True,blank=True)
#class ASUNDAY(models.Model):
    #subject = models.CharField(max_length=100)
    #starttime = models.TimeField(null=True,blank=True)
    #endtime = models.TimeField(null=True,blank=True)

class NOTE(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100,blank=True,null=False)
    tital = models.CharField(max_length=100,blank=True,null=False)
    datetime = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='Note')
    comment = models.CharField(max_length=350,blank=True,null=False)
    
class NOTIFICATION(models.Model):
    name = models.CharField(max_length=100)
    tital = models.CharField(max_length=100,blank=True,null=False)
    subject = models.CharField(max_length=100,blank=True,null=False)
    day = models.CharField(blank=True,null=False,choices=DAY_CHOICES,max_length=20)
    date = models.DateField(blank=True,null=False)
    starttime = models.TimeField(blank=True,null=False)
    endtime = models.TimeField(blank=True,null=False)
    notes = models.TextField( max_length=350,blank=True,null=False)
    link = models.URLField(max_length=200,blank=True,null=False)
    img = models.ImageField(upload_to='image',blank=True,null=False)
    file = models.FileField(upload_to='file',blank=True,null=False)
#   def __str__(self):
#        return self.name





#class NOTES(models.Model):

    #name = models.CharField(max_length=100)
    #subject = models.CharField(max_length=100)
    #tital = models.CharField(max_length=100,blank=True,null=False)
    #datetime = models.DateField(auto_now_add=True)
    #file = models.FileField(upload_to='note')
    #comment = models.TextField( blank=True,null=False)
    



