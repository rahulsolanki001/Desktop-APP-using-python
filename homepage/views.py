from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,get_user_model,login,logout
from .forms import TeacherLoginForm,TeacherSubjectForm,UserLoginForm,UserRegisterForm,StudentSubmissionForm
from django.contrib.auth.decorators import login_required
from .models import Subjects_Teaching,Assignment
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
	return render(request,'homepage/homepage.html')

def subjects(request):
	queryset=Subjects_Teaching.objects.all()
	context={'subjects':queryset}
	return render(request,'homepage/subjects.html',context)

def contact(request):
	return render(request,'homepage/tcontact.html')

def TeacherLoginView(request):
	form=TeacherLoginForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		user=authenticate(username=username,password=password)
		login(request,user)
		return redirect('Teacher_dashboard')
	return render(request,'homepage/teacher_form.html',{'form':form})

@login_required(login_url='/teacher_login/')
def TeacherDashboard(request):
	queryset=Subjects_Teaching.objects.all()
	context={'qs':queryset,}
	return render(request,'homepage/teacher_dashboard.html',context)

@login_required(login_url='/teacher_login/')
def TeacherSubjectView(request):
	form=TeacherSubjectForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		#Subjects_Teaching.objects.all().delete()
		instance.save()
		messages.success(request,'Subject Details were added Sucessfully!!')
		return redirect('Teacher_dashboard')
	return render(request,'homepage/subject_form.html',{'form':form})

@login_required(login_url='/teacher_login/')
def TeacherSubjectUpdate(request,id=None):
	instance=get_object_or_404(Subjects_Teaching,id=id)
	form=TeacherSubjectForm(request.POST or None, request.FILES or None,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		#Subjects_Teaching.objects.all().delete()
		instance.save()
		messages.success(request,'Subject Details were updated Sucessfully!!')
		return redirect('Teacher_dashboard')
	context={'instance':instance,'form':form,}
	return render(request,'homepage/subject_form.html',context)

@login_required(login_url='/teacher_login/')
def TeacherSubjectDelete(request,id=None):
	instance=get_object_or_404(Subjects_Teaching,id=id)
	instance.delete()
	messages.success(request,'Sucessfully Deleted')
	return redirect('Teacher_dashboard')

@login_required(login_url='/teacher_login/')
def TeacherAssignmentView(request):
	queryset=Assignment.objects.filter(course__course__contains='s')
	context={'qs':queryset,}
	return render(request,'homepage/assignments.html',context)
	
def teacherlogout(request):
	logout(request)
	return redirect('teacher_login')


# Create your views here.

def login_view(request):
	form=UserLoginForm(request.POST or None)
	queryset=request.user.id
	if form.is_valid():
		username=form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		user=authenticate(username=username,password=password)
		login(request,user)
		return render(request,'homepage/dashboard.html')
	context={'form':form,'qs':queryset,}
	return render(request,'homepage/form.html',context)

def register_view(request):
	form=UserRegisterForm(request.POST or None)
	if form.is_valid():
		user=form.save(commit=False)
		password=form.cleaned_data.get('password')
		user.set_password(password)
		course=form.cleaned_data.get('Choice')
		user.save()
		new_user=authenticate(username=user.username,password=password)
		login(request,new_user)
		messages.success(request,'You have been registered Sucessfully')
		return redirect('login')
	context={'form':form}
	return render(request,'homepage/registration.html',context)

def logout_view(request):
	logout(request)
	return redirect('login')
@login_required(login_url='/student_login/')
def account_view(request,username=User.username):
	#instance=get_object_or_404(User,id=id)
	return render(request,'homepage/dashboard.html')
	
@login_required(login_url='/student_login/')
def contact_view(request):
	return render(request,'homepage/contact.html')

@login_required(login_url='/student_login/')
def AssignmentView(request,id=None):
	instance=get_object_or_404(User,id=id)
	form=StudentSubmissionForm(request.POST or None, request.FILES or None,instance)
	if form.is_valid():
		form=form.save(commit=False)
		form.student=instance
		form.full_name=instance
		Assignment.objects.filter(student=form.student).delete()
		form.save()
		messages.success(request,'Assignment uploaded Sucessfully')
	#else:
		#messages.failure(request,'Please enter correct details to submit the Assignment')
		return redirect('account/')
	context={'form':form,}
	return render(request,'homepage/upload.html',context)









