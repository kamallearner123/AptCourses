from rest_framework import serializers
from .models import Course, Category, UserProfile, Enrollment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    instructor_name = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_instructor_name(self, obj):
        return obj.instructor.username if obj.instructor else None
