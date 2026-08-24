from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Examination, StudentMark
from .serializers import ExaminationSerializer, StudentMarkSerializer
from .permissions import CanEnterMarks, CanViewMarks
from .services import MarkEntryService

class ExaminationViewSet(viewsets.ModelViewSet):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer
    permission_classes = [CanViewMarks]

class StudentMarkViewSet(viewsets.ModelViewSet):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkSerializer
    permission_classes = [CanEnterMarks]
    
    def get_queryset(self):
        qs = super().get_queryset()
        exam = self.request.query_params.get('examination')
        subject = self.request.query_params.get('subject')
        stream = self.request.query_params.get('stream')
        
        if exam: qs = qs.filter(examination_id=exam)
        if subject: qs = qs.filter(subject_id=subject)
        if stream: qs = qs.filter(stream_id=stream)
        
        return qs

    @action(detail=False, methods=['post'])
    def bulk(self, request):
        marks_data = request.data.get('marks', [])
        examination_id = request.data.get('examination_id')
        subject_id = request.data.get('subject_id')
        stream_id = request.data.get('stream_id')
        
        exam = get_object_or_404(Examination, pk=examination_id)
        
        try:
            MarkEntryService.save_marks(marks_data, exam, subject_id, stream_id, request.user)
            return Response({'status': 'Marks saved successfully'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def upload(self, request):
        # Implementation for file upload
        return Response({'status': 'Not implemented yet'})

class MarkTemplateDownloadView(APIView):
    def get(self, request):
        # Return dummy excel
        return Response({'status': 'Template download not fully implemented'})

from assessments.models import KCSESchoolResult, KCSESubjectResult
from assessments.serializers import KCSESchoolResultSerializer, KCSESubjectResultSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class KCSEResultViewSet(viewsets.ModelViewSet):
    queryset = KCSESchoolResult.objects.all()
    serializer_class = KCSESchoolResultSerializer
    permission_classes = [IsAuthenticated]
