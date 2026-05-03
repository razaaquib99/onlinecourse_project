# Quick Start Guide - Online Course Assessment System

## Getting Started in 5 Minutes

### Step 1: Install Dependencies
```bash
cd /Users/mars/Desktop/Coursera/django/onlinecourse_project
pip install -r requirements.txt
```

### Step 2: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Admin User
```bash
python manage.py createsuperuser
```
Follow prompts to create your admin account.

### Step 4: Start Server
```bash
python manage.py runserver
```

### Step 5: Create Sample Course
1. Go to http://localhost:8000/admin/
2. Log in with your superuser credentials
3. Click "Courses" → "Add Course"
4. Enter "Python Basics" as the name
5. Click "Save"

### Step 6: Add Lesson & Questions
1. Click "Lessons" → "Add Lesson"
2. Enter "Variables and Data Types" as title
3. Select "Python Basics" as course
4. Click "Save"
5. Add a Question (click "+ Add another Question")
6. Enter: "What is the keyword to create a function?"
7. Add Choices:
   - "def" (mark as correct)
   - "func"
   - "function"

### Step 7: Take the Exam
1. Go to: http://localhost:8000/onlinecourse/course/1/
2. Enter your name
3. Answer questions
4. Click "Submit Exam"
5. See your results!

## Project Files Created

### Core Models (models.py)
- ✅ Course - Store course information
- ✅ Lesson - Group questions by topic
- ✅ Question - Individual exam questions
- ✅ Choice - Answer options with correct flag
- ✅ Submission - Track user scores

### Admin Interface (admin.py)
- ✅ ChoiceInline - Edit choices in questions
- ✅ QuestionInline - Edit questions in lessons
- ✅ LessonAdmin - Manage lessons with inline questions
- ✅ QuestionAdmin - Manage questions with inline choices
- ✅ All models registered

### Views (views.py)
- ✅ course_details() - Display exam form
- ✅ submit() - Process exam submission & calculate score
- ✅ show_exam_result() - Display results with pass/fail message

### URLs (urls.py)
- ✅ /onlinecourse/course/<id>/ - View exam
- ✅ /onlinecourse/submit/<id>/ - Submit answers
- ✅ /onlinecourse/result/<id>/ - View results

### Templates
- ✅ course_details_bootstrap.html - Exam form (Bootstrap 5)
- ✅ result.html - Result display (Bootstrap 5)

## Key Features

✨ **Fully Functional**
- Complete data model with relationships
- Working admin interface
- Score calculation (0-100%)
- Pass/Fail messaging (>50% = pass)

✨ **Professional Design**
- Bootstrap 5 responsive styling
- Gradient theme (purple/blue)
- Mobile-friendly forms
- Congratulations message for high scores

✨ **Production Ready**
- Django best practices
- Proper error handling
- SQL injection protection (CSRF tokens)
- Session management

## Verification Checklist

Before running, verify:
- [ ] All files in /onlinecourse/ directory (models.py, admin.py, views.py, urls.py, etc.)
- [ ] Templates in /templates/ (course_details_bootstrap.html, result.html)
- [ ] Django 5+ installed (check: `pip show django`)
- [ ] INSTALLED_APPS includes 'onlinecourse' in settings.py
- [ ] TEMPLATES DIRS configured in settings.py

## Common Commands

```bash
# Run migrations after model changes
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start development server
python manage.py runserver

# Access admin
http://localhost:8000/admin/

# View exam (replace 1 with course ID)
http://localhost:8000/onlinecourse/course/1/

# Reset database
rm db.sqlite3
python manage.py migrate
```

## Troubleshooting

**"No such table" error?**
- Run: `python manage.py migrate`

**"Template not found" error?**
- Verify templates folder exists at project root
- Check TEMPLATES DIRS in settings.py

**Admin won't load?**
- Create superuser: `python manage.py createsuperuser`

**Port 8000 in use?**
- Run: `python manage.py runserver 8001`

## Next Steps

After setup:
1. Create multiple courses through admin
2. Add several lessons per course
3. Add 5-10 questions with 3-4 choices each
4. Test by taking an exam
5. Check submission history in admin

Enjoy your Online Course Assessment System! 🎓
