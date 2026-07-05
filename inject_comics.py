import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Course, Module, Lesson

course = Course.objects.get(title="Rust on STM32")
module = Module.objects.get(course=course, order=1)

# Lesson 1.1
l1 = Lesson.objects.get(module=module, order=1)
if 'comic_m1_l1.png' not in l1.explanation_html:
    img_tag = '<img src="/static/images/comic_m1_l1.png" alt="Intro to Rust for STM32 Comic" style="width: 100%; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid rgba(0,240,255,0.3);">'
    l1.explanation_html = img_tag + "\n" + l1.explanation_html
    l1.save()
    print("Injected comic for M1.1")

# Lesson 1.2
l2 = Lesson.objects.get(module=module, order=2)
if 'comic_m1_l2.png' not in l2.explanation_html:
    img_tag = '<img src="/static/images/comic_m1_l2.png" alt="STM32 Families Comic" style="width: 100%; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid rgba(255,0,127,0.3);">'
    l2.explanation_html = img_tag + "\n" + l2.explanation_html
    l2.save()
    print("Injected comic for M1.2")

print("Comic rule implemented successfully.")
