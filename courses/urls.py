# Import necessary modules
from django.urls import path
from . import views

# Define URL patterns for courses app
urlpatterns = [
    # Course list view
    path('', views.course_list, name='course_list'),
    # Text detail view
    path('<int:course_pk>/t<int:step_pk>/', views.text_detail, name='text_detail'),
    # Quiz detail view
    path('<int:course_pk>/q<int:step_pk>/', views.quiz_detail, name='quiz_detail'),
    # Create quiz view
    path('<int:course_pk>/create_quiz/', views.quiz_create, name='create_quiz'),
    # Edit quiz view
    path('<int:course_pk>/edit_quiz<int:quiz_pk>/', views.quiz_edit, name='edit_quiz'),
    # Create question view
    path('<int:quiz_pk>/create_question/<str:question_type>/', views.create_question, name='create_question'),
    # Edit question view
    path('<int:quiz_pk>/edit_question<int:question_pk>/', views.edit_question, name='edit_question'),
    # Create answer view
    path('<int:question_pk>/create_answer/', views.answer_form, name='create_answer'),
    # Course detail view
    path('<int:pk>/', views.course_detail, name='course_detail'),
]
