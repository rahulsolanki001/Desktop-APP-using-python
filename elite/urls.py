"""elite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin 
from homepage.views import subjects,contact,TeacherDashboard,TeacherLoginView,teacherlogout,TeacherSubjectView,TeacherSubjectUpdate,TeacherSubjectDelete,login_view,register_view,account_view,logout_view,contact_view,AssignmentView,TeacherAssignmentView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage/',include('homepage.urls')),
    url(r'^subjects/',subjects,name='subjects'),
    url(r'^teacher_contact/',contact,name='contact-1'),
    url(r'^student_login/',login_view,name='login'),
    url(r'^registration/',register_view,name='registration'),
    url(r'^(?P<username>[-\w]+)/account/',account_view,name='account'),
    url(r'^logout/',logout_view,name='logout'),
    url(r'^contact/',contact_view,name='contact'),
    url(r'^teacher_login/',TeacherLoginView,name='teacher_login'),
    url(r'^dashboard/',TeacherDashboard,name='Teacher_dashboard'),
    url(r'^choosesubjects/',TeacherSubjectView,name='Teacher_Subject'),
    url(r'^teacher_logout/',teacherlogout,name='teacher_logout'),
    url(r'^(?P<id>\d+)/update/',TeacherSubjectUpdate,name='subject_update'),
    url(r'^(?P<id>\d+)/delete/',TeacherSubjectDelete,name='subject_delete'),
    url(r'^(?P<id>\d+)/upload_assignment/',AssignmentView,name='upload'),
    url(r'^assignments/',TeacherAssignmentView,name='assignments')
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
