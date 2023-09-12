from django.urls import path

from academy.apps import AcademyConfig
from rest_framework.routers import DefaultRouter

from academy.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PayCreateAPIView, PayListAPIView, PayRetrieveAPIView, PayUpdateAPIView, \
    PayDestroyAPIView

app_name = AcademyConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/retrieve/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

    path('pay/create/', PayCreateAPIView.as_view(), name='pay-create'),
    path('pay/', PayListAPIView.as_view(), name='pay-list'),
    path('pay/retrieve/<int:pk>/', PayRetrieveAPIView.as_view(), name='pay-retrieve'),
    path('pay/update/<int:pk>/', PayUpdateAPIView.as_view(), name='pay-update'),
    path('pay/delete/<int:pk>/', PayDestroyAPIView.as_view(), name='pay-delete'),

] + router.urls

