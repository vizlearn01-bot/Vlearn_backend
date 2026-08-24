from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .year_transition_service import AcademicYearTransitionService
from organizations.models import OrganizationMembership

class BaseTransitionView(APIView):
    permission_classes = [IsAuthenticated]

    def get_school(self, user):
        membership = OrganizationMembership.objects.filter(user=user).first()
        return membership.school if membership else None

class PrepareNewYearView(BaseTransitionView):
    def post(self, request):
        school = self.get_school(request.user)
        if not school:
            return Response({"error": "No school found."}, status=400)
        
        AcademicYearTransitionService.prepare_new_year(school)
        return Response({"status": "prepared"})

class TransitionPreviewView(BaseTransitionView):
    def get(self, request):
        school = self.get_school(request.user)
        if not school:
            return Response({"error": "No school found."}, status=400)
        
        preview = AcademicYearTransitionService.get_transition_preview(school)
        return Response(preview)

class HandleExceptionsView(BaseTransitionView):
    def patch(self, request):
        school = self.get_school(request.user)
        if not school:
            return Response({"error": "No school found."}, status=400)
        
        exceptions = request.data.get("exceptions", [])
        AcademicYearTransitionService.handle_exceptions(school, exceptions)
        return Response({"status": "exceptions_handled"})

class ConfirmTransitionView(BaseTransitionView):
    def post(self, request):
        school = self.get_school(request.user)
        if not school:
            return Response({"error": "No school found."}, status=400)
        
        AcademicYearTransitionService.confirm_transition(school)
        return Response({"status": "transition_confirmed"})
