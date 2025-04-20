from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import process_message
from celery.result import AsyncResult

class ProcessMessageView(APIView):
    def post(self, request):
        email = request.data.get("email")
        message = request.data.get("message")

        if not email or not message:
            return Response({"error": "Email and message are required"}, status=400)

        task = process_message
