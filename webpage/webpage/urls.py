"""webpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from web_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main_course/',views.course_detail,name="course_detail"),
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),
    path('register/',views.registration_page,name="registartion_page"),
    path('login/',views.user_login,name="Login_page"),
    path('logout/',views.user_logout,name="logout"),
    path('profile/',views.profile_page,name="profile_page"),
    path("update_profile/", views.edit_student_form, name ="student_edit_form"),
    path('Degree/',views.degree_details,name="degree_detail"),
    path('Branch/',views.branch_detail,name="branch"),
    path('Exam/',views.Exam_details,name="exam"),
    url(r'^ajax_calls/search/',views.autocompleteModel,name="auto_degree"),
    url(r'^ajax_calls/searchs/',views.autocomplte_branch,name="auto_branch"),
    url(r'^ajax_calls/search-course/',views.autocomplte_course,name="auto_course"),
    url(r'^course_profile/',views.List_view.as_view(),name="listview"),
    url(r'^managecourse/',views.managecourse,name="manage_course"),
    
    path('course/<name>',views.dynamicfield,name="dynamic-arg"),
    
    path("courses/<int:pk>", views.edit_course_form, name ="course_edit_form"),


    url(r'^course',views.dynamicfield,name="dynamic"),

    path('manage/',views.manage,name="manage"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
