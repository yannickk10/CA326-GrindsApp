from django.urls import include, path
from .views import tutor_dashboard, student_dashboard

urlpatterns = [

    path('studentdash/', include(([
            path('home/', student_dashboard.CourseListView.as_view(), name='course_home'),
            path('home/<int:pk>/', student_dashboard.CourseDetailView.as_view(), name='course_detail'),
            path('course/<int:courseid>/', student_dashboard.course_show, name='course_enroll'),
        ], 'dashboard'), namespace='studentdash')),

    path('tutordash/', include(([
        path('home/', tutor_dashboard.CourseListView.as_view(), name='home'),
        path('students', tutor_dashboard.StudentListView.as_view(), name='student_detail'),
        path('course/add', tutor_dashboard.CourseCreateView.as_view(), name='course_add'),
    ], 'dashboard'), namespace='tutordash')),
]
