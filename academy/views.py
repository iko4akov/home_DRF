from django.shortcuts import render
from rest_framework import viewsets

from academy.models import Course
from academy.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    