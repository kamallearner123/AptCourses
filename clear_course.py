import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Course

try:
    course = Course.objects.get(title="Rust on STM32")
    course.delete()
    print("Successfully deleted 'Rust on STM32' course and all its modules/lessons.")
except Course.DoesNotExist:
    print("Course 'Rust on STM32' not found. It may have already been deleted.")
