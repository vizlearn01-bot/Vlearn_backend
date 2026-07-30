from django.db import models
from Resources.models import ExperimentVideo, User


# this model contains questions for a specific video
class Quiz(models.Model):
    video = models.ForeignKey(
        ExperimentVideo, on_delete=models.CASCADE, related_name="quizzes"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # question_count = models.IntegerField(blank=True, null=True)
    # difficulty = models.TextField(default="Beginner")
    time_limit = models.IntegerField(default=15)

    def __str__(self):
        return self.title


# this model contains individual questions in the specific video
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    question_type = models.CharField(
        max_length=20,
        choices=[("MCQ", "Multiple Choice"), ("TEXT", "Text Answer")],
        default="MCQ",
    )
    points = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class QuestionAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField(null=True, blank=True)  # Duration in seconds
    score = models.FloatField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'quiz'], name='question_attempt_user_quiz_idx'),
        ]

    def __str__(self):
        return self.user.username

    @property
    def formatted_duration(self):
        if not self.duration:
            return "N/A"
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{minutes}m {seconds}s"


class StudentAnswer(models.Model):
    attempt = models.ForeignKey(
        QuestionAttempt, on_delete=models.CASCADE, related_name="student_answers"
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    text_answer = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    points_earned = models.FloatField(default=0)

    def __str__(self):
        return self.attempt.user.username
