from rest_framework import serializers

from academy.models import Course, Lesson, Subscription
from .lesson import LessonSerializer

class CourseCreateSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=True, source='lesson_set')
    class Meta:
        model = Course
        fields = ('name', 'lesson', 'description')

    def create(self, validated_data):
        lesson = validated_data.pop('lesson_set')
        course_item = Course.objects.create(**validated_data)
        user = self.context['request'].user

        for less in lesson:
            Lesson.objects.create(**less, course=course_item, owner=user)

        return course_item


class CourseSerializer(serializers.ModelSerializer):
    # count_lesson = serializers.IntegerField(source='lesson_set.count')
    count_lesson = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True)
    subscribe = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lesson(self, instance):
        if instance.lesson_set.count() > 1:
            return instance.lesson_set.count()
        return 'отсутствует'

    def get_subscribe(self, instance):
        user = self.context['request'].user
        if Subscription.objects.filter(user=user, course=instance):
            return 'True'

        else:
            return False
