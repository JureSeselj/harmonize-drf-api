from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile


class ProfileList(APIView):
    """
    A class view for the ProfileList
    """
    def get(self, request):
        profiles = Profile.objects.all()
        return Response(profiles)
