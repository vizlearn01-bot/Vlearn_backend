import re

with open("organizations/urls.py", "r") as f:
    content = f.read()

# Add viewset imports
new_views_imports = "    TeacherSpecialtyViewSet,\n    TermViewSet,\n    ExamConfigurationViewSet,\n    SetupWizardView,\n    BulkTeacherUploadView,\n    BulkStudentUploadView,\n    DownloadTemplateView,\n"
content = re.sub(r'(UnverifiedSchoolMergeView,\n)', r'\1' + new_views_imports, content)

# Register viewsets
new_routers = "router.register(r'teacher-specialties', TeacherSpecialtyViewSet, basename='teacher-specialty')\nrouter.register(r'terms', TermViewSet, basename='term')\nrouter.register(r'exam-configurations', ExamConfigurationViewSet, basename='exam-configuration')\n"
content = re.sub(r'(router.register\("invitations".*\n)', r'\1' + new_routers, content)

# Register endpoints
new_paths = "    path('setup-wizard/', SetupWizardView.as_view(), name='setup-wizard'),\n    path('bulk-upload/teachers/', BulkTeacherUploadView.as_view(), name='bulk-teacher-upload'),\n    path('bulk-upload/students/', BulkStudentUploadView.as_view(), name='bulk-student-upload'),\n    path('download-template/', DownloadTemplateView.as_view(), name='download-template'),\n"
content = re.sub(r'(path\("invitations/accept/".*\n)', r'\1' + new_paths, content)

with open("organizations/urls.py", "w") as f:
    f.write(content)

print("Patched urls.py")
