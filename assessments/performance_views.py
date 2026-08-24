from rest_framework.views import APIView
from rest_framework.response import Response
from .aggregation import PerformanceAggregator

class StudentPerformanceView(APIView):
    def get(self, request, id):
        ac_year = request.query_params.get('academic_year_id')
        term = request.query_params.get('term')
        exam = request.query_params.get('examination_id')
        data = PerformanceAggregator.student_performance(id, ac_year, term, exam)
        return Response(data)

class StreamPerformanceView(APIView):
    def get(self, request, id):
        exam = request.query_params.get('examination_id')
        data = PerformanceAggregator.stream_overall_average(id, exam)
        return Response(data)

class FormPerformanceView(APIView):
    def get(self, request, id):
        exam = request.query_params.get('examination_id')
        data = PerformanceAggregator.form_overall_average(id, exam)
        return Response(data)

class SchoolPerformanceView(APIView):
    def get(self, request, id):
        exam = request.query_params.get('examination_id')
        data = PerformanceAggregator.school_overall_average(id, exam)
        return Response(data)

class ClassTeacherStreamView(APIView):
    def get(self, request, id):
        exam = request.query_params.get('examination_id')
        data = PerformanceAggregator.stream_overall_average(id, exam)
        return Response({'stream_data': data})
