from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics

from academy.models import Course, Lesson, Pay
from academy.serializers import CourseSerializer, LessonSerializer, PaySerializer, UserPaySerializer
from user.models import User


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


class PayCreateAPIView(generics.CreateAPIView):
    serializer_class = PaySerializer

class PayListAPIView(generics.ListAPIView):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson', 'course')
    ordering_fields = ('date',)

class PayRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()


class PayUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()


class PayDestroyAPIView(generics.DestroyAPIView):
    queryset = Pay.objects.all()


class UserPayListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserPaySerializer
