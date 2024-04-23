from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import AddContentSerializer
from .models import AddCourse
import json


class AddContentView(APIView):
    
    
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        serializer = AddContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseListAPI(APIView):
#    @permission_classes([IsAuthenticated])
    
#    authentication_classes = [ExpiringTokenAuthentication]
    permission_classes = [IsAuthenticated]

    @method_decorator(csrf_exempt)
    def get(self, request):
        user = request.user
#        course_names = AddContent.objects.values_list('content_id','content_name')

        course_names = AddCourse.objects.filter(user_id = self.request.user.pk).values_list('content_id','content_name')     

        formatted_course_names = {int(content_id): content_name for content_id, content_name in course_names}

        return Response(formatted_course_names,status=status.HTTP_200_OK)
    


'''

from django.http import JsonResponse
from django.views import View
from .models import FairchatHistory

class FetchFairchatData(View):
    def get(self, request):
        try:
            data = FairchatHistory.objects.all().order_by('-q_id').values()
            return JsonResponse(list(data), safe=False)
        except Exception as e:
            return JsonResponse({"message": "An error occurred"}, status=500)


'''




""" class LogTestAPI(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request):


        db_logger = logging.getLogger('db')

        db_logger.info('info message')
        db_logger.warning('warning message')

        try:
            1/0
        except Exception as e:
            db_logger.exception(e)


        print('Log test')
        return Response({'data': True}, status=status.HTTP_200_OK) """