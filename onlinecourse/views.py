from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Course, Submission, Question, Choice, Enrollment


def course_details(request, course_id):
    """
    Display course details with exam questions.
    
    Args:
        request: HTTP request object
        course_id: ID of the course to display
        
    Returns:
        Rendered course_details_bootstrap.html template with course data
    """
    # Get the course or return 404 if not found
    course = get_object_or_404(Course, id=course_id)
    
    # Create context with course data
    context = {
        'course': course,
    }
    
    return render(request, 'course_details_bootstrap.html', context)


def submit(request, course_id):
    """
    Handle exam submission by calculating score and saving submission.
    
    Args:
        request: HTTP request object containing POST data with selected answers
        course_id: ID of the course being submitted
        
    Returns:
        Redirects to show_exam_result view after processing submission
    """
    # Get the course or return 404 if not found
    course = get_object_or_404(Course, id=course_id)
    
    # Get user name from request
    user_name = request.POST.get('user_name', 'Anonymous User')
    
    # Create or get enrollment
    enrollment, created = Enrollment.objects.get_or_create(
        user=user_name,
        course=course
    )
    
    # Create submission linked to enrollment
    submission = Submission.objects.create(
        enrollment=enrollment
    )
    
    # Get all questions for this course through lessons
    questions = Question.objects.filter(lesson__course=course)
    
    # Collect selected choice IDs and add to submission
    selected_choice_ids = []
    for question in questions:
        # Get the selected choice ID from POST data
        selected_choice_id = request.POST.get(f'choice_{question.id}')
        if selected_choice_id:
            selected_choice_ids.append(selected_choice_id)
    
    # Add selected choices to submission's M2M relationship
    if selected_choice_ids:
        submission.choices.set(selected_choice_ids)
    
    # Store submission ID in session to display in result page
    request.session['last_submission_id'] = submission.id
    
    # Redirect to result page
    return redirect('show_exam_result', course_id=course_id)


def show_exam_result(request, course_id):
    """
    Display the exam result and score to the user with detailed breakdown.
    
    Args:
        request: HTTP request object
        course_id: ID of the course for which result is being shown
        
    Returns:
        Rendered result.html template with score, grade, questions, and selected choices
    """
    # Get the course or return 404 if not found
    course = get_object_or_404(Course, id=course_id)
    
    # Get last submission from session
    submission_id = request.session.get('last_submission_id')
    submission = None
    if submission_id:
        submission = Submission.objects.filter(id=submission_id).first()
    
    # Get all selected choices from submission
    selected_choices = submission.choices.all() if submission else []
    selected_ids = list(selected_choices.values_list('id', flat=True))
    
    # Get all questions for this course
    questions = Question.objects.filter(lesson__course=course)
    
    total_score = 0
    possible_score = questions.count()
    
    # Calculate score by checking if selected choices match correct answers
    for question in questions:
        correct_choices = question.choices.filter(is_correct=True)
        question_selected_choices = selected_choices.filter(question=question)
        
        # Check if selected choices match correct choices for this question
        if set(correct_choices.values_list('id', flat=True)) == set(question_selected_choices.values_list('id', flat=True)):
            total_score += 1
    
    # Calculate grade percentage
    grade = (total_score / possible_score * 100) if possible_score > 0 else 0
    
    # Determine if user passed (score > 50%)
    passed = grade > 50
    
    # Create context for template with all required variables
    context = {
        'course': course,
        'score': total_score,
        'total': possible_score,
        'grade': int(grade),
        'passed': passed,
        'selected_ids': selected_ids,
        'questions': questions,
    }
    
    return render(request, 'result.html', context)
