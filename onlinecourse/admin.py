from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission


class ChoiceInline(admin.TabularInline):
    """
    Inline admin for Choice model to manage choices within questions.
    """
    model = Choice
    extra = 1


class QuestionInline(admin.TabularInline):
    """
    Inline admin for Question model to manage questions within lessons.
    """
    model = Question
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    """
    Admin interface for Question model with inline choices.
    """
    inlines = [ChoiceInline]
    list_display = ('question_text', 'lesson')
    search_fields = ('question_text',)


class LessonAdmin(admin.ModelAdmin):
    """
    Admin interface for Lesson model with inline questions.
    """
    inlines = [QuestionInline]
    list_display = ('title', 'course')
    search_fields = ('title',)


class CourseAdmin(admin.ModelAdmin):
    """
    Admin interface for Course model.
    """
    list_display = ('name',)
    search_fields = ('name',)


class SubmissionAdmin(admin.ModelAdmin):
    """
    Admin interface for Submission model to view submission records.
    """
    list_display = ('user_name', 'course', 'score', 'created_at')
    search_fields = ('user_name', 'course__name')
    list_filter = ('course', 'created_at')
    readonly_fields = ('created_at',)


# Register all models with their respective admin classes
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)
