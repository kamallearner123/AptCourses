import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Course, Module, Lesson

course = Course.objects.get(title="Rust on STM32")
module = Module.objects.get(course=course, order=1)
l2 = Lesson.objects.get(module=module, order=2)

original = l2.explanation_html

# Remove the specific Unsplash image tag
# We can use regex to remove any unsplash image in this section just to be safe,
# or match the specific URL
pattern = r'<img src="https://images\.unsplash\.com/photo-1555664424-778a1e5e1b48[^>]+>'
new_html = re.sub(pattern, '', original)

if original != new_html:
    l2.explanation_html = new_html
    l2.save()
    print("Successfully removed the Arduino image from M1.2!")
else:
    print("Image not found or already removed.")
