#!/usr/bin/env python
"""
Script to create sample course data for testing the Online Course system.
Run this after migrations: python manage.py shell < create_sample_data.py
"""

from onlinecourse.models import Course, Lesson, Question, Choice

# Clear existing data (optional)
# Course.objects.all().delete()

# Create course
course = Course.objects.create(name="Python Basics")

# Create lesson
lesson = Lesson.objects.create(course=course, title="Variables and Data Types")

# Create question 1
q1 = Question.objects.create(lesson=lesson, question_text="What is a variable?")
Choice.objects.create(question=q1, choice_text="A named container for storing data", is_correct=True)
Choice.objects.create(question=q1, choice_text="A type of loop", is_correct=False)
Choice.objects.create(question=q1, choice_text="A function definition", is_correct=False)

# Create question 2
q2 = Question.objects.create(lesson=lesson, question_text="Which is a valid variable name?")
Choice.objects.create(question=q2, choice_text="my_var", is_correct=True)
Choice.objects.create(question=q2, choice_text="2var", is_correct=False)
Choice.objects.create(question=q2, choice_text="var-name", is_correct=False)

print("✅ Sample data created successfully!")
print(f"Course ID: {course.id}")
print(f"Access the exam at: http://127.0.0.1:8000/onlinecourse/course/{course.id}/")
