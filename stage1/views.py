from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from datetime import datetime


# Create your views here.
@api_view(['GET'])
def student_info(request):
        slack_name = request.query_params.get("slack_name")
        track = request.query_params.get("backend")

        data = {
            " slack_name": "slack_name",
            "current_day": datetime.today().strftime("%A"),
            "utc_time": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),           
            "track": 'backend',
            "github": 'sghssjs',
            "status": 200,
        
        }
        return Response(data)



