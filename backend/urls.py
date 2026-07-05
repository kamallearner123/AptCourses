"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from courses.views import landing_page, course_detail, course_learn, user_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls')),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('course/<int:course_id>/learn/', course_learn, name='course_learn'),
    path('course/<int:course_id>/learn/<int:lesson_id>/', course_learn, name='course_learn_lesson'),
    path('', landing_page, name='landing'),
]
