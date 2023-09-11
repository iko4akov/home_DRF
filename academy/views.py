from rest_framework import viewsets, generics

from academy.models import Course, Lesson, Pay
from academy.serializers import CourseSerializer, LessonSerializer, LessonPaySerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()

class LessonPayListAPIView(generics.ListAPIView):
    queryset = Pay.objects.filter(lesson__isnull=False)
    serializer_class = LessonPaySerializer
