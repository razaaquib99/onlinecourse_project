from django.db import models


class Course(models.Model):
    """
    Course model to represent an online course with a name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Lesson(models.Model):
    """
    Lesson model representing a lesson within a course.
    Multiple lessons can belong to a single course.
    """
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"


class Question(models.Model):
    """
    Question model representing a question within a lesson.
    Multiple questions can belong to a single lesson.
    """
    question_text = models.CharField(max_length=500)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Choice(models.Model):
    """
    Choice model representing an answer choice for a question.
    Multiple choices can belong to a single question.
    """
    choice_text = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"


class Submission(models.Model):
    """
    Submission model to store exam submission results.
    Tracks user submissions and their scores.
    """
    user_name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='submissions')
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.course.name} - Score: {self.score}"

    class Meta:
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"
