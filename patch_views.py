import re

with open("organizations/views.py", "r") as f:
    content = f.read()

# Add imports for new models
new_models_imports = "    TeacherSpecialty,\n    Term,\n    ExamConfiguration,\n"
content = re.sub(r'(SchoolInvitation,\n)', r'\1' + new_models_imports, content)

new_serializers_imports = "    TeacherSpecialtySerializer,\n    TermSerializer,\n    ExamConfigurationSerializer,\n    SetupWizardStateSerializer,\n    BulkTeacherUploadSerializer,\n    BulkStudentUploadSerializer,\n"
content = re.sub(r'(SchoolInvitationSerializer,\n)', r'\1' + new_serializers_imports, content)

new_services_imports = "from organizations.services import EntitlementService, SchoolOnboardingService, BulkUploadService"
content = re.sub(r'from organizations.services import EntitlementService, SchoolOnboardingService', new_services_imports, content)

# Import IsSchoolAdmin
new_perm_imports = "from rest_framework.permissions import IsAuthenticated\nfrom organizations.permissions import IsSchoolAdmin"
content = re.sub(r'from rest_framework.permissions import IsAuthenticated', new_perm_imports, content)

# Also need HTTP_200_OK etc from status, which are already imported
# Add new views at the end of the file

new_views = """

class TeacherSpecialtyViewSet(viewsets.ModelViewSet):
    queryset = TeacherSpecialty.objects.all().order_by('-created_at')
    serializer_class = TeacherSpecialtySerializer
    permission_classes = [IsAuthenticated, IsSchoolAdmin]

    def get_queryset(self):
        qs = super().get_queryset()
        school_id = self.request.query_params.get('school') or self.request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(school_id=school_id)
        return qs


class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all().order_by('academic_year', 'number')
    serializer_class = TermSerializer
    permission_classes = [IsAuthenticated, IsSchoolAdmin]

    def get_queryset(self):
        qs = super().get_queryset()
        school_id = self.request.query_params.get('school') or self.request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(school_id=school_id)
        return qs


class ExamConfigurationViewSet(viewsets.ModelViewSet):
    queryset = ExamConfiguration.objects.all().order_by('-created_at')
    serializer_class = ExamConfigurationSerializer
    permission_classes = [IsAuthenticated, IsSchoolAdmin]

    def get_queryset(self):
        qs = super().get_queryset()
        school_id = self.request.query_params.get('school') or self.request.query_params.get('school_id')
        if school_id:
            qs = qs.filter(school_id=school_id)
        return qs


class SetupWizardView(APIView):
    permission_classes = [IsAuthenticated, IsSchoolAdmin]

    def get(self, request):
        school_id = request.query_params.get('school_id')
        if not school_id:
            return Response({"detail": "school_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        school = School.objects.filter(id=school_id).first()
        if not school:
            return Response({"detail": "School not found."}, status=status.HTTP_404_NOT_FOUND)
            
        return Response({
            "current_step": school.setup_wizard_step,
            "school_data": SchoolSerializer(school).data
        }, status=status.HTTP_200_OK)

    def patch(self, request):
        school_id = request.data.get('school_id')
        step = request.data.get('step')
        if not school_id or step is None:
            return Response({"detail": "school_id and step are required."}, status=status.HTTP_400_BAD_REQUEST)
            
        school = School.objects.filter(id=school_id).first()
        if not school:
            return Response({"detail": "School not found."}, status=status.HTTP_404_NOT_FOUND)
            
        school.setup_wizard_step = int(step)
        school.save(update_fields=['setup_wizard_step'])
        
        return Response({
            "current_step": school.setup_wizard_step,
            "detail": "Setup wizard step updated successfully."
        }, status=status.HTTP_200_OK)


class BulkTeacherUploadView(APIView):
    permission_classes = [IsAuthenticated, IsSchoolAdmin]
    
    def post(self, request):
        serializer = BulkTeacherUploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        school_id = serializer.validated_data['school']
        file_obj = serializer.validated_data['file']
        
        school = School.objects.filter(id=school_id).first()
        if not school:
            return Response({"detail": "School not found."}, status=status.HTTP_404_NOT_FOUND)
            
        try:
            rows = BulkUploadService.parse_file(file_obj)
            created, errors = BulkUploadService.import_teachers(school, rows)
            return Response({"created": created, "errors": errors}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BulkStudentUploadView(APIView):
    permission_classes = [IsAuthenticated, IsSchoolAdmin]
    
    def post(self, request):
        serializer = BulkStudentUploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        stream_id = serializer.validated_data['stream']
        file_obj = serializer.validated_data['file']
        
        stream = Stream.objects.filter(id=stream_id).select_related('school_class__school').first()
        if not stream:
            return Response({"detail": "Stream not found."}, status=status.HTTP_404_NOT_FOUND)
            
        school = stream.school_class.school
        
        # Get current academic year
        academic_year = AcademicYear.objects.filter(school=school, is_current=True).first()
        if not academic_year:
            academic_year = AcademicYear.objects.filter(school=school).first()
            if not academic_year:
                return Response({"detail": "No academic year found for this school."}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            rows = BulkUploadService.parse_file(file_obj)
            created, errors = BulkUploadService.import_students(school, stream, academic_year, rows)
            return Response({"created": created, "errors": errors}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DownloadTemplateView(APIView):
    permission_classes = [IsAuthenticated, IsSchoolAdmin]
    
    def get(self, request):
        import openpyxl
        from django.http import HttpResponse
        
        template_type = request.query_params.get('type')
        if template_type not in ['teacher', 'student']:
            return Response({"detail": "Invalid type. Must be 'teacher' or 'student'."}, status=status.HTTP_400_BAD_REQUEST)
            
        wb = openpyxl.Workbook()
        ws = wb.active
        
        if template_type == 'teacher':
            ws.title = "Teacher Upload Template"
            headers = ['Teacher Name', 'Phone Number', 'Email', 'TSC Number', 'Subject Specialties']
            example = ['John Doe', '+254700000000', 'john@example.com', '123456', 'Mathematics, Physics']
        else:
            ws.title = "Student Upload Template"
            headers = ['Student Name', 'Admission Number']
            example = ['Jane Doe', 'ADM-001']
            
        ws.append(headers)
        ws.append(example)
        
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={template_type}_upload_template.xlsx'
        wb.save(response)
        
        return response
"""

content += new_views

with open("organizations/views.py", "w") as f:
    f.write(content)

print("Patched views.py")
