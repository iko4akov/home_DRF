from rest_framework import serializers

from academy.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    # count_lesson = serializers.IntegerField(source='lesson_set.count')
    count_lesson = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lesson(self, instance):
        if instance.lesson_set.count() > 1:
            return instance.lesson_set.count()
        return 'отсутствует'



class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
