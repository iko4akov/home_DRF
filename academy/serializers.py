from rest_framework import serializers

from academy.models import Course, Lesson, Pay
from user.models import User


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


class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pay
        fields = '__all__'

class UserPaySerializer(serializers.ModelSerializer):
    pay = PaySerializer(source='pay_set', many=True)
    class Meta:
        model = User
        fields = ('email', 'pay')

