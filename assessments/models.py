from django.db import models
from django.conf import settings

class Examination(models.Model):
    EXAM_STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('published', 'Published')
    ]
    TERM_CHOICES = [
        (1, 'Term 1'),
        (2, 'Term 2'),
        (3, 'Term 3'),
    ]

    school = models.ForeignKey('organizations.School', on_delete=models.CASCADE, related_name='assessment_examinations', null=True, blank=True)
    academic_year = models.ForeignKey('organizations.AcademicYear', on_delete=models.CASCADE, related_name='assessment_examinations', null=True, blank=True)
    term = models.PositiveIntegerField(choices=TERM_CHOICES, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    sequence = models.PositiveIntegerField(default=1, null=True, blank=True)
    max_score = models.PositiveIntegerField(default=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default='open', choices=EXAM_STATUS_CHOICES, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        unique_together = ('school', 'academic_year', 'term', 'sequence')

    def __str__(self):
        return f"{self.name} - {self.academic_year} (Term {self.term})"

class ExaminationSubject(models.Model):
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE, related_name='subject_configs', null=True, blank=True)
    subject = models.ForeignKey('curriculum.Subject', on_delete=models.CASCADE, related_name='exam_configs', null=True, blank=True)
    max_score = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('examination', 'subject')

    def __str__(self):
        return f"{self.examination} - {self.subject}"

class StudentMark(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_marks', null=True, blank=True)
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE, related_name='marks', null=True, blank=True)
    subject = models.ForeignKey('curriculum.Subject', on_delete=models.CASCADE, related_name='student_marks', null=True, blank=True)
    stream = models.ForeignKey('organizations.Stream', on_delete=models.CASCADE, related_name='student_marks', null=True, blank=True)
    academic_year = models.ForeignKey('organizations.AcademicYear', on_delete=models.CASCADE, related_name='student_marks', null=True, blank=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    max_score = models.PositiveIntegerField(default=100, null=True, blank=True)
    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='entered_marks', null=True, blank=True)
    entered_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        unique_together = ('student', 'examination', 'subject')
        indexes = [
            models.Index(fields=['examination', 'subject', 'stream']),
        ]

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.score}"

class KCSESchoolResult(models.Model):
    school = models.ForeignKey('organizations.School', on_delete=models.CASCADE, related_name='kcse_results', null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    mean_grade = models.CharField(max_length=5, null=True, blank=True)
    mean_points = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    total_candidates = models.PositiveIntegerField(default=0, null=True, blank=True)
    grade_a_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    grade_a_minus_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    grade_b_plus_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    grade_b_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    grade_b_minus_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    grade_c_plus_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    grade_c_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    grade_c_minus_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    grade_d_plus_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    grade_d_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    grade_d_minus_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    grade_e_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        unique_together = ('school', 'year')
        ordering = ['-year']

class KCSESubjectResult(models.Model):
    school_result = models.ForeignKey(KCSESchoolResult, on_delete=models.CASCADE, related_name='subject_results', null=True, blank=True)
    subject = models.ForeignKey('curriculum.Subject', on_delete=models.CASCADE, null=True, blank=True)
    mean_grade = models.CharField(max_length=5, null=True, blank=True)
    mean_points = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    candidates = models.PositiveIntegerField(default=0, null=True, blank=True)

    class Meta:
        unique_together = ('school_result', 'subject')
