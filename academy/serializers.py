from rest_framework import serializers

from academy.models import Course, Lesson, Pay


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # count_lesson = serializers.IntegerField(source='lesson_set.count')
    count_lesson = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lesson(self, instance):
        if instance.lesson_set.count() > 1:
            return instance.lesson_set.count()
        return 'отсутствует'


class LessonPaySerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    class Meta:
        model = Pay
        fields = '__all__'

class CourseCreateSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        lesson = validated_data.pop('lesson_set')

        course_item = Course.objects.creaye(**validated_data)

        for les in lesson:
            Lesson.objects.create(**les, course=course_item)

        return course_item

