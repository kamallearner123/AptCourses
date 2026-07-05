from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render
from .models import Course, Category
from .serializers import CourseSerializer, CategorySerializer

def landing_page(request):
    courses = Course.objects.filter(status='published')[:6]
    return render(request, 'courses/landing.html', {'courses': courses})

def user_dashboard(request):
    # For now, just show all published courses as "My Courses"
    courses = Course.objects.filter(status='published')
    return render(request, 'courses/dashboard.html', {'courses': courses})

from django.shortcuts import get_object_or_404

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

def course_learn(request, course_id, lesson_id=None):
    course = get_object_or_404(Course, id=course_id)
    modules = course.modules.all().prefetch_related('lessons')
    
    current_lesson = None
    if lesson_id:
        from .models import Lesson
        current_lesson = get_object_or_404(Lesson, id=lesson_id, module__course=course)
    else:
        # Default to first lesson of first module
        first_module = modules.first()
        if first_module:
            current_lesson = first_module.lessons.first()
            
    return render(request, 'courses/course_learn.html', {
        'course': course, 
        'modules': modules,
        'current_lesson': current_lesson
    })


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(status='published')
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # We can add filtering by category, level, price etc here
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset
