import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Lesson

def transform_mcqs(html):
    # This regex looks for <br> followed by <strong>Answer: (or just Answer:)
    # and captures everything until the closing </li>
    
    # Many of them have <br><strong>Answer: B</strong>...</li>
    # Some might not have <br>, so we'll optionally match <br>\s*
    pattern = r'(?:<br>\s*)?(<strong>Answer:.*?)?(?=</li>)'
    
    # Actually, a safer regex:
    # Match `<br><strong>Answer:` up to `</li>`
    pattern_strict = r'<br>\s*(<strong>Answer:.*?)(?=</li>)'
    
    replacement = r'''
    <details style="margin-top: 0.75rem; margin-bottom: 0.5rem;">
        <summary style="cursor: pointer; color: var(--primary-color); font-size: 0.9rem; font-weight: 600; list-style-type: '👉 ';">Show Answer & Explanation</summary>
        <div style="margin-top: 0.5rem; padding: 0.75rem; background: rgba(0, 240, 255, 0.05); border-left: 3px solid var(--primary-color); border-radius: 4px; color: #fff;">
            \1
        </div>
    </details>
    '''
    
    # We will do a regex sub
    new_html = re.sub(pattern_strict, replacement, html, flags=re.IGNORECASE | re.DOTALL)
    
    # Also handle cases where there is no <br> before Answer:
    pattern_fallback = r'(<strong>Answer:.*?)?(?=</li>)'
    # Only run fallback if strict didn't hit something? 
    # Actually strict should hit all of them based on our seed scripts.
    
    return new_html

lessons = Lesson.objects.all()

for lesson in lessons:
    if lesson.mcqs_html:
        new_mcq = transform_mcqs(lesson.mcqs_html)
        if new_mcq != lesson.mcqs_html:
            lesson.mcqs_html = new_mcq
            lesson.save()
            print(f"Updated MCQs for: {lesson.title}")

print("Rule 3: MCQ Answers hidden successfully.")
