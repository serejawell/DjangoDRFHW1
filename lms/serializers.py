from rest_framework import serializers

from lms.models import Course, Lesson, Subscription
from lms.validators import validate_youtube_url


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для уроков"""
    video_link = serializers.CharField(validators=[validate_youtube_url])

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = []


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для курсов"""
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_subscribed(self, obj):
        """Проверяем, есть ли подписка у текущего пользователя на этот курс."""
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False


class CourseDetailSerializer(serializers.ModelSerializer):
    '''Создаем новый сериализатор для вывода кол-ва уроков'''
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, course):
        return course.lessons.count()

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'image', 'lessons_count', 'lessons')
