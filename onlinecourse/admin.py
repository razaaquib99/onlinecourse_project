from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Enrollment, Submission


class ChoiceInline(TabularInline):
    """
    Inline admin for Choice model to manage choices within questions.
    """
    model = Choice
    extra = 1


class QuestionInline(TabularInline):
    """
    Inline admin for Question model to manage questions within lessons.
    """
    model = Question
    extra = 1


class QuestionAdmin(ModelAdmin):
    """
    Admin interface for Question model with inline choices.
    """
    inlines = [ChoiceInline]
    list_display = ('question_text', 'lesson')
    search_fields = ('question_text',)


class LessonAdmin(ModelAdmin):
    """
    Admin interface for Lesson model with inline questions.
    """
    inlines = [QuestionInline]
    list_display = ('title', 'course')
    search_fields = ('title',)


class CourseAdmin(ModelAdmin):
    """
    Admin interface for Course model.
    """
    list_display = ('name',)
    search_fields = ('name',)


class SubmissionAdmin(ModelAdmin):
    """
    Admin interface for Submission model to view submission records.
    """
    list_display = ('enrollment', 'id')
    search_fields = ('enrollment__user', 'enrollment__course__name')
    list_filter = ('enrollment__course',)


# Register all models with their respective admin classes
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Enrollment)
admin.site.register(Submission, SubmissionAdmin)
