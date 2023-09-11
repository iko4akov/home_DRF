from django.core.management import BaseCommand

from academy.models import Course, Lesson


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        list_course = [
            {'pk': 1, 'name': 'Python-developer', 'description': 'python3'},
            {'pk': 2, 'name': 'GO-developer', 'description': 'java'},
            {'pk': 3, 'name': 'java-developer', 'description': 'java'},
        ]

        course_for_create = []

        for items_course in list_course:
            course_for_create.append(Course(**items_course))

        Course.objects.bulk_create(course_for_create)

        list_lesson = [
            {'pk': 1, 'name': 'Python', 'description': 'Python-developer', 'course': Course.objects.get(pk=1)},
            {'pk': 2, 'name': 'Django', 'description': 'Python-developer', 'course': Course.objects.get(pk=1)},
            {'pk': 3, 'name': 'Flask', 'description': 'Python-developer', 'course': Course.objects.get(pk=1)},
            {'pk': 4, 'name': 'Linux', 'description': 'GO-developer', 'course': Course.objects.get(pk=2)},
            {'pk': 5, 'name': 'windows', 'description': 'GO-developer', 'course': Course.objects.get(pk=2)},
            {'pk': 6, 'name': 'HTML', 'description': 'JAVA-developer', 'course': Course.objects.get(pk=3)},
        ]

        lesson_for_create = []

        for items_course in list_lesson:
            lesson_for_create.append(Lesson(**items_course))

        Lesson.objects.bulk_create(lesson_for_create)
