from django.db import models
from django.conf import settings

# Create your models here.

def upload_location(instance,filename):
	return '%s/%s' %(instance.id,filename)

class Subject(models.Model):
	subject=models.CharField(blank=False,verbose_name='subject',max_length=30)
	Course=models.CharField(blank=False,verbose_name='Course-sem',max_length=20)


	def __str__(self):
		return str(self.subject)


course=[('PMCS-1','PMCS-1'),('PMCS-2','PMCS-2'),('PMCS-3','PMCS-3'),('PMCS-4','PMCS-4'),('PMCS-5','PMCS-5'),('PMCS-6','PMCS-6'),('CS-1','CS-1'),('CS-2','CS-2'),('CS-3','CS-3'),('CS-4','CS-4'),('CS-5','CS-5'),('CS-6','CS-6'),]
class Subjects_Teaching(models.Model):
	subject=models.CharField(blank=False,verbose_name='subject',max_length=40)
	assignment_given=models.FileField(blank=False,verbose_name='Assignment',upload_to=upload_location)
	solution=models.FileField(blank=False,verbose_name='Solution',upload_to=upload_location)
	date_of_submission=models.DateField(auto_now=False,verbose_name='Last Date of Submission')
	course=models.CharField(choices=course,max_length=6)

	def __str__(self):
		return str(self.course)

#from django.contrib.auth.models import User
# Create your models here.


#course=[('PMCS-1','PMCS-1'),('PMCS-2','PMCS-2'),('PMCS-3','PMCS-3'),('PMCS-4','PMCS-4'),('PMCS-5','PMCS-5'),('PMCS-6','PMCS-6'),('CS-1','CS-1'),('CS-2','CS-2'),('CS-3','CS-3'),('CS-4','CS-4'),('CS-5','CS-5'),('CS-6','CS-6'),]

class Assignment(models.Model):
	student=models.ForeignKey(settings.AUTH_USER_MODEL)
	roll_no=models.CharField(max_length=10,verbose_name='Roll NO')
	full_name=models.CharField(max_length=40,verbose_name='FULL NAME')
	course=models.ForeignKey(Subjects_Teaching)
	assignment=models.FileField(upload_to=upload_location)
	time_stamp=models.DateField(auto_now=True)

#	class Meta:
#		unique_together=['student','roll_no','full_name']

	def __str__(self):
		return str(self.course)




