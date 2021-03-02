from django.urls import include, path
from .views import welcome, tutor, students

urlpatterns = [
    path('', welcome.welcome_view, name='welcome'),
    path('contact/', welcome.contact_view, name='contact'),

    path('students/', include(([
            path('home/', students.CourseListView.as_view(), name='course_home'),
            path('home/<int:pk>/', students.CourseDetailView.as_view(), name='course_detail'),
        ], 'quiz'), namespace='students')),

    path('tutor/', include(([
        path('home/', tutor.home, name='home'),
        path('course/add', tutor.CourseCreateView.as_view(), name='course_add'),
    ], 'quiz'), namespace='tutor')),
]
