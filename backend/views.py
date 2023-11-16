from django.shortcuts import render
from rest_framework import viewsets
from .models import Feedback
from .serializer import FeedbackSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def FeedbackViewSet(request):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer(queryset, many=True)
    return Response(serializer_class.data)
