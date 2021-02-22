from django.urls import include, path
from .views import tutor, students

urlpatterns = [

    path('students/', include(([
            path('', students.QuizListView.as_view(), name='quiz_list'),
            path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
            path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
        ], 'quiz'), namespace='students')),


    path('tutor/', include(([
        path('', tutor.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', tutor.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', tutor.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', tutor.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', tutor.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', tutor.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', tutor.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', tutor.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'quiz'), namespace='tutor')),
]
