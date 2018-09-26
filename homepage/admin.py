from django.contrib import admin
from .models import Subject,Subjects_Teaching
from .models import Assignment
# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
	list_display=('subject1','subject2',)
	list_filter=['subject1']


class subjectadmin(admin.ModelAdmin):
	list_display=('subject','Course',)
	list_filter=['Course']

class TeachingAdmin(admin.ModelAdmin):
	list_display=('subject','assignment_given','solution','date_of_submission','course')
	list_filter=['subject']


class assignment_admin(admin.ModelAdmin):
	list_display=('student','roll_no','full_name','course','assignment','time_stamp')
	list_filter=['roll_no']

admin.site.register(Assignment,assignment_admin)
admin.site.register(Subject,subjectadmin)
admin.site.register(Subjects_Teaching,TeachingAdmin)


