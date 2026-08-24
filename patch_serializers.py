import re

with open("organizations/serializers.py", "r") as f:
    content = f.read()

# Add imports for new models
new_imports = "    TeacherSpecialty,\n    Term,\n    ExamConfiguration,\n"
content = re.sub(r'(SchoolInvitation,\n)', r'\1' + new_imports, content)

new_serializers = """

class TeacherSpecialtySerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    teacher_name = serializers.CharField(source='teacher.get_full_name', read_only=True)

    class Meta:
        model = TeacherSpecialty
        fields = ['id', 'teacher', 'subject', 'school', 'subject_name', 'teacher_name', 'created_at']
        read_only_fields = ['created_at']


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ['id', 'school', 'academic_year', 'name', 'number', 'start_date', 'end_date', 'is_current']


class ExamConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamConfiguration
        fields = ['id', 'school', 'academic_year', 'term', 'exam_count', 'exam_definitions', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class SetupWizardStateSerializer(serializers.Serializer):
    \"\"\"Serializer for the setup wizard state.\"\"\"
    current_step = serializers.IntegerField()
    step_data = serializers.DictField(required=False)
    

class BulkTeacherUploadSerializer(serializers.Serializer):
    \"\"\"Serializer for bulk teacher CSV/Excel upload.\"\"\"
    file = serializers.FileField()
    school = serializers.IntegerField()


class BulkStudentUploadSerializer(serializers.Serializer):
    \"\"\"Serializer for bulk student CSV/Excel upload.\"\"\"
    file = serializers.FileField()
    stream = serializers.IntegerField()
"""

content += new_serializers

with open("organizations/serializers.py", "w") as f:
    f.write(content)

print("Patched serializers.py")
