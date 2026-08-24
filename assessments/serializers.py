from rest_framework import serializers
from .models import Examination, StudentMark

class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = '__all__'

class StudentMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMark
        fields = '__all__'

from assessments.models import KCSESchoolResult, KCSESubjectResult

class KCSESubjectResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = KCSESubjectResult
        fields = '__all__'

class KCSESchoolResultSerializer(serializers.ModelSerializer):
    subject_results = KCSESubjectResultSerializer(many=True, read_only=True)

    class Meta:
        model = KCSESchoolResult
        fields = '__all__'
