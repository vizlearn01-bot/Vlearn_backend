from django.db import transaction
from .models import StudentMark
from django.core.exceptions import ValidationError

class MarkEntryService:
    @staticmethod
    def validate_marks(marks_data, examination, subject, stream):
        # marks_data is a list of dicts: {'student_id': 1, 'score': 85.0}
        # Check scores > max_score or < 0
        max_score = examination.max_score
        for item in marks_data:
            score = item.get('score')
            if score is None:
                continue
            if score > max_score or score < 0:
                raise ValidationError(f"Score {score} is out of bounds (0 - {max_score})")

        # In a real app we might also check for missing students in the stream, duplicates, etc.
        student_ids = [item['student_id'] for item in marks_data]
        if len(student_ids) != len(set(student_ids)):
            raise ValidationError("Duplicate student entries found in marks data.")

        return True

    @staticmethod
    @transaction.atomic
    def save_marks(marks_data, examination, subject, stream, teacher):
        MarkEntryService.validate_marks(marks_data, examination, subject, stream)
        
        subj_id = getattr(subject, 'id', subject)
        st_id = getattr(stream, 'id', stream)
        
        for item in marks_data:
            student_id = item['student_id']
            score = item['score']
            
            StudentMark.objects.update_or_create(
                student_id=student_id,
                examination=examination,
                subject_id=subj_id,
                defaults={
                    'stream_id': st_id,
                    'academic_year': examination.academic_year,
                    'score': score,
                    'max_score': examination.max_score,
                    'entered_by': teacher
                }
            )

    @staticmethod
    def parse_upload(file, stream):
        # Dummy parsing for example purposes
        # Reads excel/csv and returns list of dicts [{'student_id': x, 'score': y}]
        # Actual implementation would use pandas or csv module
        return []
