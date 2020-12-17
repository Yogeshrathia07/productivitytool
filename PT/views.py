from django.contrib.auth.models import User,auth
from django.core.checks import messages
from django.forms.fields import DateField, DateTimeField
from django.http import request
from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import files
#from .models import NOTES
from.models import MONDAY, TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY, NOTIFICATION, WEDNESDAY,NOTE
# Create your views here.

 
def home(request):

           return render(request,'index.html') 
def about(request):
    return render(request,'about.html')
def timetable(request):

      #tt=TIMETABLE.objects.all()
      #mon=MONDAY.objects.all()
        mon=MONDAY.objects.order_by('starttime')#.filter(day__iexact='Monday')     
        #mon=TIMETABLE.objects.order_by('day')
        tue=TUESDAY.objects.order_by('starttime')#.filter(day__iexact='Tuesday')
        wed=WEDNESDAY.objects.order_by('starttime')#.filter(day__iexact='Wednesday')
        thu=THURSDAY.objects.order_by('starttime')#.filter(day__iexact='Thursday')
        fri=FRIDAY.objects.order_by('starttime')#.filter(day__iexact='Friday')
        sat=SATURDAY.objects.order_by('starttime')#.filter(day__iexact='SATURDAY')
        sun=SUNDAY.objects.order_by('starttime')#.all().filter(day__iexact='Sunday')
        return render(request,'timetable1.html',{'n1':mon,'n2':tue,'n3':wed,'n4':thu,'n5':fri,'n6':sat,'n7':sun})

def notification(request):
    noti=NOTIFICATION.objects.all()
    return render(request, "notification.html",{'n8':noti})

def notes(request):
    if request.method == "POST":
        form = files(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = files()
    fl=NOTE.objects.order_by('datetime')
    return render(request,'notes.html',{'fl':fl,'form':form}) 

#def delete(request, id):
 #   if request.method == "POST":
  #      pi = User.objects.get(pk=id)
   #     pi.delete()
    #    return HttpResponseRedirect('/')        

def delete(request, pk):
    if request.method == 'POST':
        pi = NOTE.objects.get(pk=pk)
        pi.delete()
    return redirect('/notes')





    