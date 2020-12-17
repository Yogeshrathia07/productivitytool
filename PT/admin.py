from django.contrib import admin
from.models import MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY,NOTIFICATION,NOTE


# Register your models here.
#from.models import DATA, NOTIFICATION
#admin.site.register(DATA)
#admin.site.register(NOTIFICATION)
#admin.site.register(TIMETABLE)
from.models import NOTIFICATION
@admin.register(NOTIFICATION)
class NOTIFICATION(admin.ModelAdmin):
    list_display=['name','tital','subject']

from.models import MONDAY
@admin.register(MONDAY)
class TIMETABLE(admin.ModelAdmin):
    list_display=['subject','starttime','endtime']

from.models import TUESDAY
@admin.register(TUESDAY)
class TIMETABLE(admin.ModelAdmin):
    list_display=['subject','starttime','endtime']


from.models import WEDNESDAY
@admin.register(WEDNESDAY)
class TIMETABLE(admin.ModelAdmin):
    list_display=['subject','starttime','endtime']

from.models import THURSDAY
@admin.register(THURSDAY)
class TIMETABLE(admin.ModelAdmin):
    list_display=['subject','starttime','endtime']


from.models import FRIDAY
@admin.register(FRIDAY)
class TIMETABLE(admin.ModelAdmin):
    list_display=['subject','starttime','endtime']


from.models import SATURDAY
@admin.register(SATURDAY)
class TIMETABLE(admin.ModelAdmin):
    list_display=['subject','starttime','endtime']

from.models import SUNDAY
@admin.register(SUNDAY)
class TIMETABLE(admin.ModelAdmin):
    list_display=['subject','starttime','endtime']

#from.models import ASUNDAY
#@admin.register(ASUNDAY)
#class TIMETABLE(admin.ModelAdmin):
 #   list_display=['subject','starttime','endtime']    

@admin.register(NOTE)
class note(admin.ModelAdmin):
    list_display = ['id','name','subject','tital','datetime']

