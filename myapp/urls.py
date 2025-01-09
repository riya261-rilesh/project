"""crowd_funding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('login/', views.login),
    path('login_post/', views.login_post),
    path('admin_home/', views.admin_home),
    path('admin_change_password/', views.admin_change_password),
    path('admin_change_password_post/', views.admin_change_password_post),
    path('complaint_reply/<int:id>', views.complaint_reply),
    path('complaint_reply_post/', views.complaint_reply_post),
    path('admin_view_complaints/', views.admin_view_complaints),
    path('admin_view_complaints_search/', views.admin_view_complaints_search),
    path('view_user/', views.view_user),
    path('search_user/', views.search_user),



    path('signup/', views.signup),
    path('signup_post/', views.signup_post),
    path('user_home/', views.user_home),
    path('view_user_profile/', views.view_user_profile),
    path('view_edit_profile/', views.edit_profile),
    path('view_edit_profile_post/', views.editprofilepost),
    path('user_change_password/', views.change_password),
    path('user_password_post/', views.change_password_post),
    path('sent_complaint/', views.sent_complaint),
    path('sent_complaint_post/', views.sent_complaint_post),
    path('user_view_reply/', views.user_view_reply),
    path('user_view_replysearch/',views.user_view_replysearch),


    path('logout/',views.logout),
    path('start/',views.start),
    path('fileupload/',views.fileupload),
    path('fileuploadpost/',views.fileuploadpost),
    path('user_view_sentfiles/',views.user_view_sentfiles),
    path('user_view_sentfiles_search/',views.user_view_sentfiles_search),
    path('user_download_file/<id>',views.user_download_file),
    path('userdownloadpost/',views.userdownloadpost),
    path('user_view_inbox/',views.user_view_inbox),


    path('user_add_group/',views.user_add_group),
    path('user_view_groups/',views.user_view_groups),
    path('user_search_view_members/<grpid>',views.user_search_view_members),
    path('use_search_view_members/',views.use_search_view_members),
    path('addtogrp/<uid>',views.addtogrp),
    path('user_view_grpmembers/<id>',views.user_view_grpmembers),
    path('user_view_grpmembers_search/',views.user_view_grpmembers_search),
    path('deletegroup/<gid>',views.deletegroup),
    path('group_fileupload/',views.group_fileupload),
    path('group_fileuploadpost/',views.group_fileuploadpost),
    path('group_view_files/<id>',views.group_view_files),
    path('group_download_files/<fileid>/<grpid>',views.group_download_files),
    path('group_download_filepost/',views.group_download_filepost),
    path('user_view_grpmembers_post/',views.user_view_grpmembers_post),


]