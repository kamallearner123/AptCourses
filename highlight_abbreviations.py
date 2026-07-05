import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Lesson

abbreviations = [
    "HAL", "PAC", "ADC", "I2C", "SPI", "DMA", "MCU", "GPIO", 
    "DSP", "FPU", "RTOS", "SRAM", "UART", "LLVM", "ADAS", "ECU", 
    "V2X", "OTA", "CMSIS", "NVIC", "SVD", "DSP"
]

# We need a regex that matches these words, but we must ensure we don't 
# replace them if they are already inside our span class, or inside an anchor href.
# A safe way: use a regex that finds text outside of tags.
def highlight_text(html):
    # Regex to find these abbreviations. \b is word boundary.
    pattern = r'\b(' + '|'.join(abbreviations) + r')\b'
    
    # We will split by HTML tags, process the text chunks, and reassemble.
    parts = re.split(r'(<[^>]+>)', html)
    for i, part in enumerate(parts):
        # Even indices are text outside tags
        if i % 2 == 0:
            parts[i] = re.sub(pattern, r'<span class="abbr-highlight">\1</span>', part)
            
    return "".join(parts)

lessons = Lesson.objects.all()

for lesson in lessons:
    updated = False
    
    if lesson.explanation_html:
        new_html = highlight_text(lesson.explanation_html)
        if new_html != lesson.explanation_html:
            lesson.explanation_html = new_html
            updated = True
            
    if lesson.challenges_html:
        new_html = highlight_text(lesson.challenges_html)
        if new_html != lesson.challenges_html:
            lesson.challenges_html = new_html
            updated = True
            
    if lesson.assignments_html:
        new_html = highlight_text(lesson.assignments_html)
        if new_html != lesson.assignments_html:
            lesson.assignments_html = new_html
            updated = True
            
    if lesson.mcqs_html:
        new_html = highlight_text(lesson.mcqs_html)
        if new_html != lesson.mcqs_html:
            lesson.mcqs_html = new_html
            updated = True
            
    if updated:
        lesson.save()
        print(f"Highlighted abbreviations in: {lesson.title}")

print("Abbreviation highlighting complete.")
