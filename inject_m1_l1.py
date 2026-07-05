import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Course, Module, Lesson

course = Course.objects.get(title="Rust on STM32")
module = Module.objects.get(course=course, order=1)
lesson = Lesson.objects.get(module=module, order=1)

with open('m1_l1_content.html', 'r') as f:
    content = f.read()

lesson.explanation_html = content
lesson.save()

print(f"Successfully injected corporate training textbook content into {lesson.title}!")
