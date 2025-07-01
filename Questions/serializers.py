from rest_framework import serializers
from .models import Answer, Question , Quiz, QuestionAttempt, StudentAnswer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'is_correct'] 
    

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)  # Nested answers
    
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text', 'answers']  

class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = ['id', 'question', 'answer', 'text_answer', 'is_correct', 'points_earned']

class QuizSerializer(serializers.ModelSerializer):
    questions= QuestionSerializer(many=True, read_only=True)
    question_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Quiz
        fields = ['id', 'video', 'title', 'description', 'time_limit','difficulty', 'question_count', 'questions']  
          
    def get_question_count(self, obj):
        return obj.questions.count()

class QuestionAttemptSerializer(serializers.ModelSerializer):
    student_answers = StudentAnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)
    
    class Meta:
        model = QuestionAttempt
        fields = ['id', 'user', 'quiz', 'duration', 'score', 'is_completed', 'student_answers']

