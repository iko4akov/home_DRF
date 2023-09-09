from academy.apps import AcademyConfig
from rest_framework.routers import DefaultRouter

from academy.views import CourseViewSet

app_name = AcademyConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [

] + router.urls

