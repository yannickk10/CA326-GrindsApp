"""django_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from users import views as user_views
from quiz.views import tutor, students
from dashboard.views import welcome, tutor, students


urlpatterns = [
    path('', include('quiz.urls')),
    path('', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('login/', user_views.login_page, name="login"),
    path('student-register/', user_views.student_register, name="student-register"),
    path('tutor-register/', user_views.tutor_register, name="tutor-register"),
]
