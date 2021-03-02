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
from dashboard import views as dashboard_view
from quiz.views import tutor



urlpatterns = [
    path('', include('quiz.urls')),
    path('', home_views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('login/', user_views.login_page, name="login"),
    path('student-register/', user_views.student_register, name="student-register"),
    path('tutor-register/', user_views.tutor_register, name="tutor-register"),
    path('contact-page/', home_views.contact_view, name="contact-page"),
    path('tutor-dashboard/', dashboard_view.tutor_dash_view, name="tutor-dash-page"),
    path('student-dashboard/', dashboard_view.student_dash_view, name="student-dash-page")
]
