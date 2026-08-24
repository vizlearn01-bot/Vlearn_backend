from django.db.models import Avg
from .models import StudentMark
from .grading import grade_from_score

class PerformanceAggregator:
    @staticmethod
    def student_performance(student_id, academic_year_id, term=None, examination_id=None):
        qs = StudentMark.objects.filter(student_id=student_id, academic_year_id=academic_year_id)
        if term:
            qs = qs.filter(examination__term=term)
        if examination_id:
            qs = qs.filter(examination_id=examination_id)
        
        avg = qs.aggregate(avg_score=Avg('score'))['avg_score'] or 0.0
        avg_float = round(float(avg), 1)
        return {
            'average': avg_float,
            'avg_score': avg_float,
            'grade': grade_from_score(avg_float)
        }

    @staticmethod
    def student_subject_history(student_id, subject_id, academic_year_id):
        return list(StudentMark.objects.filter(
            student_id=student_id, 
            subject_id=subject_id, 
            academic_year_id=academic_year_id
        ).values('examination__name', 'score', 'examination__term', 'entered_at').order_by('examination__sequence'))

    @staticmethod
    def stream_subject_average(stream_id, subject_id, examination_id=None):
        qs = StudentMark.objects.filter(stream_id=stream_id, subject_id=subject_id)
        if examination_id:
            qs = qs.filter(examination_id=examination_id)
        avg = qs.aggregate(avg_score=Avg('score'))['avg_score'] or 0.0
        avg_float = round(float(avg), 1)
        return {
            'average': avg_float,
            'avg_score': avg_float,
            'grade': grade_from_score(avg_float)
        }

    @staticmethod
    def stream_overall_average(stream_id, examination_id=None):
        qs = StudentMark.objects.filter(stream_id=stream_id)
        if examination_id:
            qs = qs.filter(examination_id=examination_id)
        avg = qs.aggregate(avg_score=Avg('score'))['avg_score'] or 0.0
        avg_float = round(float(avg), 1)
        return {
            'average': avg_float,
            'avg_score': avg_float,
            'grade': grade_from_score(avg_float)
        }

    @staticmethod
    def form_subject_average(school_class_id, subject_id, examination_id=None):
        qs = StudentMark.objects.filter(stream__school_class_id=school_class_id, subject_id=subject_id)
        if examination_id:
            qs = qs.filter(examination_id=examination_id)
        avg = qs.aggregate(avg_score=Avg('score'))['avg_score'] or 0.0
        avg_float = round(float(avg), 1)
        return {
            'average': avg_float,
            'avg_score': avg_float,
            'grade': grade_from_score(avg_float)
        }

    @staticmethod
    def form_overall_average(school_class_id, examination_id=None):
        qs = StudentMark.objects.filter(stream__school_class_id=school_class_id)
        if examination_id:
            qs = qs.filter(examination_id=examination_id)
        avg = qs.aggregate(avg_score=Avg('score'))['avg_score'] or 0.0
        avg_float = round(float(avg), 1)
        return {
            'average': avg_float,
            'avg_score': avg_float,
            'grade': grade_from_score(avg_float)
        }

    @staticmethod
    def school_subject_average(school_id, subject_id, examination_id=None):
        qs = StudentMark.objects.filter(examination__school_id=school_id, subject_id=subject_id)
        if examination_id:
            qs = qs.filter(examination_id=examination_id)
        avg = qs.aggregate(avg_score=Avg('score'))['avg_score'] or 0.0
        avg_float = round(float(avg), 1)
        return {
            'average': avg_float,
            'avg_score': avg_float,
            'grade': grade_from_score(avg_float)
        }

    @staticmethod
    def school_overall_average(school_id, examination_id=None):
        qs = StudentMark.objects.filter(examination__school_id=school_id)
        if examination_id:
            qs = qs.filter(examination_id=examination_id)
        avg = qs.aggregate(avg_score=Avg('score'))['avg_score'] or 0.0
        avg_float = round(float(avg), 1)
        return {
            'average': avg_float,
            'avg_score': avg_float,
            'grade': grade_from_score(avg_float)
        }

    @staticmethod
    def student_longitudinal_record(student_id):
        return list(StudentMark.objects.filter(student_id=student_id).values(
            'academic_year__year', 'examination__name', 'subject__name', 'score'
        ).order_by('academic_year__year', 'examination__sequence'))
