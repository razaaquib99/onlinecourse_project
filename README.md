# Online Course Assessment System

A complete Django project implementing an Online Course system with an assessment (exam) feature. This system allows users to take course exams, submit answers, and receive immediate feedback on their performance.

## Features

- **Course Management**: Create and organize courses with multiple lessons
- **Lesson Organization**: Group questions into lessons within courses
- **Assessment System**: Create multiple-choice questions with correct answer tracking
- **Exam Submission**: Users can take exams by submitting their answers
- **Score Calculation**: Automatic calculation of exam scores based on correct answers
- **Result Display**: Show exam results with congratulations message if score > 50%
- **Submission History**: Store all user submissions in the database
- **Admin Interface**: Fully functional Django admin with inline editing for nested relationships

## Project Structure

```
onlinecourse_project/
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── db.sqlite3                     # SQLite database (created after migrations)
│
├── onlinecourse_project/         # Main project configuration
│   ├── __init__.py
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Main URL router
│   ├── asgi.py
│   └── wsgi.py
│
├── onlinecourse/                 # Django app for the course system
│   ├── __init__.py
│   ├── models.py                 # Database models
│   ├── admin.py                  # Admin interface configuration
│   ├── views.py                  # View functions
│   ├── urls.py                   # App URL patterns
│   ├── apps.py                   # App configuration
│   ├── tests.py                  # Unit tests
│   └── migrations/               # Database migrations
│       └── __init__.py
│
└── templates/                    # HTML templates
    ├── course_details_bootstrap.html  # Exam form with Bootstrap styling
    └── result.html                    # Exam result display
```

## Models

### Course
- `name` (CharField): Name of the course

### Lesson
- `title` (CharField): Title of the lesson
- `course` (ForeignKey): Reference to parent Course

### Question
- `question_text` (CharField): The question text
- `lesson` (ForeignKey): Reference to parent Lesson

### Choice
- `choice_text` (CharField): Text of the answer choice
- `question` (ForeignKey): Reference to parent Question
- `is_correct` (BooleanField): Whether this choice is the correct answer

### Submission
- `user_name` (CharField): Name of the user who submitted
- `course` (ForeignKey): Reference to the Course being submitted
- `score` (IntegerField): Percentage score (0-100)
- `created_at` (DateTimeField): Timestamp of submission

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation Steps

1. **Navigate to the project directory**:
   ```bash
   cd /Users/mars/Desktop/Coursera/django/onlinecourse_project
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   # On macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate
   
   # On Windows:
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations to create the database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser for admin access**:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to enter username, email, and password.

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Admin Interface: http://localhost:8000/admin/
   - Course Details: http://localhost:8000/onlinecourse/course/[course_id]/
   - Submit Exam: http://localhost:8000/onlinecourse/submit/[course_id]/
   - View Results: http://localhost:8000/onlinecourse/result/[course_id]/

## Usage Guide

### Creating Course Content via Admin

1. **Log in to Admin Interface**:
   - Go to http://localhost:8000/admin/
   - Use the superuser credentials created during setup

2. **Add a Course**:
   - Click on "Courses" and click "Add Course"
   - Enter a course name (e.g., "Python Basics")
   - Click "Save"

3. **Add Lessons**:
   - Click on "Lessons" and click "Add Lesson"
   - Enter lesson title (e.g., "Variables and Data Types")
   - Select the course
   - Click "Save"

4. **Add Questions**:
   - In the Lessons admin, click on a lesson
   - Under "Questions", click "Add another Question"
   - Enter question text
   - Click "Save and Continue"

5. **Add Answer Choices**:
   - In the Questions admin, click on a question
   - Under "Choices", add multiple choices
   - Check "is_correct" for the correct answer
   - Click "Save"

### Taking an Exam

1. **Access the exam form**:
   - Visit http://localhost:8000/onlinecourse/course/[course_id]/
   - Replace `[course_id]` with the actual course ID

2. **Complete the exam**:
   - Enter your name
   - Select one answer for each question
   - Click "Submit Exam"

3. **View results**:
   - See your score percentage
   - If score > 50%, you'll see a congratulations message
   - Use "Back to Exam" button to retake the exam

## URL Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/admin/` | GET | Django admin interface |
| `/onlinecourse/course/<id>/` | GET | Display course exam form |
| `/onlinecourse/submit/<id>/` | POST | Submit exam answers |
| `/onlinecourse/result/<id>/` | GET | Display exam results |

## Admin Features

The admin interface includes:

- **Course Admin**: View and manage all courses
- **Lesson Admin**: Manage lessons with inline question editing
- **Question Admin**: Manage questions with inline choice editing
- **Choice Admin**: Manage individual answer choices
- **Submission Admin**: View all student submissions with filtering and search

## Styling

The application uses Bootstrap 5.3.0 for responsive, professional styling:
- Modern gradient backgrounds (purple/blue theme)
- Responsive cards and form layouts
- Interactive hover effects
- Mobile-friendly design

## Features Highlighted

✅ **Complete Models**: Course, Lesson, Question, Choice, Submission with proper relationships
✅ **Admin Interface**: Full inline editing support for nested relationships
✅ **Score Calculation**: Automatic percentage calculation based on correct answers
✅ **Result Display**: Dynamic feedback with pass/fail messaging
✅ **Session Management**: Uses Django sessions to persist submission data
✅ **Bootstrap Styling**: Professional, responsive UI design
✅ **Django Best Practices**: Comments, proper structure, error handling
✅ **Django 5+ Compatible**: Works with the latest Django version

## Troubleshooting

### Database errors
If you encounter database errors, reset the database:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Template not found errors
Make sure the templates directory exists at the project root and contains the HTML files.

### Port already in use
To run on a different port:
```bash
python manage.py runserver 8001
```

## Database Schema

The application uses SQLite with the following tables:
- `onlinecourse_course`
- `onlinecourse_lesson`
- `onlinecourse_question`
- `onlinecourse_choice`
- `onlinecourse_submission`

## Django Settings

Key settings configured in `settings.py`:
- **DEBUG**: True (for development)
- **INSTALLED_APPS**: Includes 'onlinecourse'
- **DATABASES**: SQLite3 database (db.sqlite3)
- **TEMPLATES**: Configured to use BASE_DIR/templates and APP_DIRS
- **TIME_ZONE**: UTC

## Example Data Creation

You can create sample data through the admin interface:

1. Create a "Python 101" course
2. Add "Introduction" lesson
3. Add question: "What is the output of print(2 + 2)?"
   - Choice A: "3" (incorrect)
   - Choice B: "4" (correct)
   - Choice C: "22" (incorrect)
4. Add more questions as needed
5. Test by accessing the course exam page

## Future Enhancements

Potential improvements could include:
- User authentication system
- Timed exams
- Question randomization
- Partial credit scoring
- Exam attempt history per user
- Question categories
- Image/rich text support
- Export results to CSV
- Email notifications

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions, review the code comments which provide detailed explanations of functionality.
