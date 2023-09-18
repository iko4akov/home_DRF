from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics

from academy.models import Course, Lesson, Pay, Subscription
from academy.permissions import IsModerator, IsOwner, IsOwnerOrStaff
from academy.serializers import CourseSerializer, LessonSerializer, PaySerializer, UserPaySerializer, \
    CourseCreateSerializer
from academy.serializers.subscription import SubscriptionSerializer
from user.models import User


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = []
    def get_queryset(self):
        if self.action == 'list':
            if self.request.user.is_staff:
                return Course.objects.all()
            else:
                return Course.objects.filter(owner=self.request.user.pk)
        else:
            return Course.objects.all()


    def create(self, request, *args, **kwargs):
        self.serializer_class = CourseCreateSerializer
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.action == 'create':
            return [IsModerator()]
        elif self.action == 'destroy':
            return [IsOwner()]
        elif self.action == 'retrieve' or self.action == 'update':
            return [IsOwnerOrStaff()]
        else:
            return []




class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsModerator]
    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    def get_queryset(self):
        if self.request.user.is_staff:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=self.request.user.pk)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]



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

class SubscriptionCreateAPIView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionListAPIView(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
