"""
URL configuration for hw_hillel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from courses_app import views as courses_views
from members_app import views as members_views
from members_with_db_app import views as members_db_views
from home import views as home_views

members_patterns = [
    path('', members_views.members_page, name='members'),
    path('input/', members_views.input_page, name='input_page'),
    path('input/display/', members_views.display_page, name='display_page'),
    path('session/', members_views.session_page, name='session_page')
]

members_db_patterns = [
    path('', members_db_views.members_page, name='members'),
    path('input/', members_db_views.input_page, name='input_page'),
    path('input/display/', members_db_views.display_page, name='display_page'),
    path('all_message_page/', members_db_views.all_message_page, name='all_message_page')
]

urlpatterns = [
    path('', home_views.home_page, name='home_page'),
    path('admin/', admin.site.urls),
    path('courses/', courses_views.authenticated, name='courses_index'),
    path('members/', include(members_patterns)),
    path('members_db/', include(members_db_patterns))
]
