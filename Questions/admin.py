from django.contrib import admin
from .models import Question, Quiz, QuestionAttempt, StudentAnswer, Answer

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuestionAttempt)
admin.site.register(StudentAnswer)
admin.site.register(Answer)