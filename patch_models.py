import re

with open("organizations/models.py", "r") as f:
    content = f.read()

# Add to School model
# We look for:
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
school_field = '\n    setup_wizard_step = models.PositiveIntegerField(default=0, help_text="Current step in the setup wizard (0=not started, 1-8=step number)")\n'
content = re.sub(r'(\s+created_at = models\.DateTimeField\(auto_now_add=True\))', school_field + r'\1', content)

# Add to SchoolInvitation model
# We look for:
#     email = models.EmailField()
invitation_field = '\n    phone_number = models.CharField(max_length=20, null=True, blank=True, help_text="Phone number for SMS-based invitations")\n'
content = re.sub(r'(\s+email = models\.EmailField\(\))', r'\1' + invitation_field, content)

# Append new models
new_models = """

class TeacherSpecialty(models.Model):
    \"\"\"Records a teacher's subject specialization. Informational only -- does NOT restrict assignment.\"\"\"
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='specialties')
    subject = models.ForeignKey('curriculum.Subject', on_delete=models.CASCADE, related_name='specialist_teachers')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teacher_specialties')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('teacher', 'subject', 'school')
        verbose_name_plural = 'Teacher specialties'

    def __str__(self):
        return f"{self.teacher.get_full_name()} - {self.subject.name}"


class Term(models.Model):
    \"\"\"Academic term within a school year. Kenyan schools have 3 terms.\"\"\"
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='terms')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='terms')
    name = models.CharField(max_length=50)  # e.g. "Term 1"
    number = models.PositiveIntegerField()  # 1, 2, or 3
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)

    class Meta:
        unique_together = ('school', 'academic_year', 'number')
        ordering = ['academic_year', 'number']

    def __str__(self):
        return f"{self.school.name} - {self.academic_year.name} - {self.name}"


class ExamConfiguration(models.Model):
    \"\"\"Configures the examination structure for a school per term.\"\"\"
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='exam_configurations')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='exam_configurations')
    term = models.PositiveIntegerField()  # 1, 2, or 3
    exam_count = models.PositiveIntegerField(default=3)
    exam_definitions = models.JSONField(
        default=list,
        help_text='List of exam definitions: [{"name": "Opening Exam", "sequence": 1}, ...]'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('school', 'academic_year', 'term')

    def __str__(self):
        return f"{self.school.name} - {self.academic_year.name} Term {self.term} Exams"
"""

content += new_models

with open("organizations/models.py", "w") as f:
    f.write(content)

print("Patched models.py")
