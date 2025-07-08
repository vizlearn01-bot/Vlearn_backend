from django.contrib import admin
from .models import Question, Quiz, QuestionAttempt, StudentAnswer, Answer

# Register your models here.


class AnswerInLine(admin.StackedInline):
    model = Answer
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]
    

class QuestionInline(admin.TabularInline):
    model = Question
    show_change_link = True
    can_delete = False
    extra = 0
    

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionAttempt)
admin.site.register(StudentAnswer)
