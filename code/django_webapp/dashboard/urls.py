from django.urls import include, path
from .views import tutor_dashboard, student_dashboard

urlpatterns = [

<<<<<<< HEAD
    path('student-dashboard/', include(([
            path('home/', students.CourseListView.as_view(), name='course_home'),
            path('home/<int:pk>/', students.CourseDetailView.as_view(), name='course_detail'),
        ], 'quiz'), namespace='student-dashboard')),
=======
    path('studentdash/', include(([
            path('home/', student_dashboard.CourseListView.as_view(), name='course_home'),
            path('home/<int:pk>/', student_dashboard.CourseDetailView.as_view(), name='course_detail'),
        ], 'quiz'), namespace='studentdash')),
>>>>>>> develop

    path('tutordash/', include(([
        path('home/', tutor_dashboard.home, name='home'),
        path('course/add', tutor_dashboard.CourseCreateView.as_view(), name='course_add'),
    ], 'quiz'), namespace='tutordash')),
]
