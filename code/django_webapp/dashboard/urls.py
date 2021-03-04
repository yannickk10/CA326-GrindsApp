from django.urls import include, path
from .views import tutor_dashboard, student_dashboard

urlpatterns = [

    path('studentdash/', include(([
            path('home/', student_dashboard.CourseListView.as_view(), name='course_home'),
            path('home/<int:pk>/', student_dashboard.CourseDetailView.as_view(), name='course_detail'),
        ], 'dashboard'), namespace='studentdash')),

    path('tutordash/', include(([
        path('home/', tutor_dashboard.CourseCreateView.as_view(), name='home'),
        path('course/add', tutor_dashboard.CourseCreateView.as_view(), name='course_add'),
    ], 'dashboard'), namespace='tutordash')),
]
