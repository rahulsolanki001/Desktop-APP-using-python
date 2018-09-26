from django import forms
from django.contrib.auth import authenticate,get_user_model,login,logout
from .models import Subjects_Teaching
from .models import Assignment
from django.contrib.auth.models import User
import datetime as dt


class TeacherLoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username=self.cleaned_data.get('username')
		password=self.cleaned_data.get('password')
		
		#user_qs=User.objects.filter(username=username)
		#if user_qs.count()==1:
			#user=user_qs.first()
		if username and password:
			user=authenticate(username=username,password=password)
			if not user:
				raise forms.ValidationError('This user does not exist')

			if not user.check_password(password):
				raise forms.ValidationError('Incorrect Password')

			if not user.is_active:
				raise forms.ValidationError('The User is no longer active')

			if not user.is_staff:
				raise forms.ValidationError('Only Teachers are  allowed to login here')
		return super(TeacherLoginForm,self).clean(*args,**kwargs)

class TeacherSubjectForm(forms.ModelForm):

	class Meta:
		model=Subjects_Teaching
		fields=['subject','assignment_given','solution','date_of_submission','course']


user=get_user_model()
class UserLoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username=self.cleaned_data.get('username')
		password=self.cleaned_data.get('password')
		
		#user_qs=User.objects.filter(username=username)
		#if user_qs.count()==1:
			#user=user_qs.first()
		if username and password:
			user=authenticate(username=username,password=password)
			if not user:
				raise forms.ValidationError('This user does not exist')

			if not user.check_password(password):
				raise forms.ValidationError('Incorrect Password')

			if not user.is_active:
				raise forms.ValidationError('The User is no longer active')
		return super(UserLoginForm,self).clean(*args,**kwargs)

class UserRegisterForm(forms.ModelForm):
	#pno=forms.IntegerField()
	password=forms.CharField(widget=forms.PasswordInput)
	password1=forms.CharField(widget=forms.PasswordInput,label='confirm password')
	first_name=forms.CharField(required=True)
	last_name=forms.CharField(required=True)
	email=forms.CharField(required=True)
	
	class Meta:
		#widget={'username':forms.TextInput(attrs={'placeholder':'Enter Username','class':'form-control'}),
				#'email':forms.EmailInput(attrs={'placeholder':'Email','class':'form-control'}),
				
				#}

		model=user
		fields=['username','first_name','last_name','email','password','password1',]

	def clean(self):
		cleaned_data=super(UserRegisterForm,self).clean()
		password=cleaned_data.get('password')
		password1=cleaned_data.get('password1')

		if password != password1:
			raise forms.ValidationError('Password does not match')

		if len(password) < 8:
			raise forms.ValidationError('Password must be atleast 8 characters long')


class StudentSubmissionForm(forms.ModelForm):
	class Meta:
		model=Assignment
		fields=['roll_no','course','assignment',]

	# def clean(self):
	# 	cleaned_data=self.cleaned_data
	# 	date_of_submission=cleaned_data.get('date_of_submission')
	# 	time_stamp=cleaned_data.get('time_stamp')
	# 	if time_stamp > date_of_submission:
	# 		raise forms.ValidationError('Last Date to upload assignment has been over!!...')


