import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Lesson

def transform_mcqs_global(html):
    # Match any variation of "Answer: " up to the </li>
    # (e.g. "Answer: A", "<strong>Answer: B</strong>")
    # We use (?:<br>\s*)? to optionally consume a preceding <br> tag so it doesn't leave an empty line
    # We use (?:<strong>)? to optionally consume a preceding strong tag
    
    # Let's just find "Answer:" (with optional strong/br before it)
    pattern = r'(?:<br>\s*)?(?:<strong>)?\s*(Answer:\s*.*?)(?=</li>)'
    
    replacement = r'''
    <details style="margin-top: 0.75rem; margin-bottom: 0.5rem;">
        <summary style="cursor: pointer; color: var(--primary-color); font-size: 0.9rem; font-weight: 600; list-style-type: '👉 ';">Show Answer & Explanation</summary>
        <div style="margin-top: 0.5rem; padding: 0.75rem; background: rgba(0, 240, 255, 0.05); border-left: 3px solid var(--primary-color); border-radius: 4px; color: #fff;">
            <strong>\1
        </div>
    </details>
    '''
    
    # We must be careful because if it was already processed, it will have `<summary>` in it.
    if "<summary" in html:
        return html # Already processed
        
    return re.sub(pattern, replacement, html, flags=re.IGNORECASE | re.DOTALL)

lessons = Lesson.objects.all()

for lesson in lessons:
    if lesson.mcqs_html:
        new_mcq = transform_mcqs_global(lesson.mcqs_html)
        if new_mcq != lesson.mcqs_html:
            lesson.mcqs_html = new_mcq
            lesson.save()
            print(f"Updated MCQs for: {lesson.title}")

print("Rule 3: MCQ Answers hidden successfully for all lessons.")
