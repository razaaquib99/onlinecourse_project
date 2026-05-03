from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Course, Submission, Question, Choice


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
    
    # Get all questions for this course through lessons
    questions = Question.objects.filter(lesson__course=course)
    
    # Initialize score counter
    score = 0
    total_questions = questions.count()
    
    # Iterate through all questions and check selected answers
    for question in questions:
        # Get the selected choice ID from POST data
        # The form sends choice IDs with key format: f"choice_{question.id}"
        selected_choice_id = request.POST.get(f'choice_{question.id}')
        
        if selected_choice_id:
            try:
                selected_choice = Choice.objects.get(id=selected_choice_id)
                # Check if the selected choice is correct
                if selected_choice.is_correct:
                    score += 1
            except Choice.DoesNotExist:
                pass
    
    # Calculate percentage score
    if total_questions > 0:
        percentage = (score / total_questions) * 100
    else:
        percentage = 0
    
    # Get or create user name from request (you can customize this)
    user_name = request.POST.get('user_name', 'Anonymous User')
    
    # Create and save the submission record
    submission = Submission.objects.create(
        user_name=user_name,
        course=course,
        score=int(percentage)  # Store as percentage
    )
    
    # Store submission ID in session to display in result page
    request.session['last_submission_id'] = submission.id
    request.session['last_score'] = int(percentage)
    
    # Redirect to result page
    return redirect('show_exam_result', course_id=course_id)


def show_exam_result(request, course_id):
    """
    Display the exam result and score to the user.
    
    Args:
        request: HTTP request object
        course_id: ID of the course for which result is being shown
        
    Returns:
        Rendered result.html template with score and congratulations message if applicable
    """
    # Get the course or return 404 if not found
    course = get_object_or_404(Course, id=course_id)
    
    # Get the score from session (set in submit view)
    score = request.session.get('last_score', 0)
    
    # Determine if user passed (score > 50%)
    passed = score > 50
    
    # Create context for template
    context = {
        'course': course,
        'score': score,
        'passed': passed,
    }
    
    return render(request, 'result.html', context)
