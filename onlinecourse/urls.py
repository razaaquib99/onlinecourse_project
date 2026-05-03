from django.urls import path
from . import views

# URL patterns for the onlinecourse app
urlpatterns = [
    # URL for viewing course details and exam questions
    path('course/<int:course_id>/', views.course_details, name='course_details'),
    
    # URL for exam submission
    path('submit/<int:course_id>/', views.submit, name='submit'),
    
    # URL for displaying exam results
    path('result/<int:course_id>/', views.show_exam_result, name='show_exam_result'),
]
