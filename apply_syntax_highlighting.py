import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Lesson

lessons = Lesson.objects.all()

for lesson in lessons:
    updated = False
    
    if lesson.explanation_html:
        original = lesson.explanation_html
        
        # We know M1.1 has a C code block. Let's specifically target it.
        # Find the C example
        if "// C Example: Buffer Overflow" in original:
            original = original.replace(
                '<pre style="background: #111; padding: 1rem; border-radius: 8px; color: #00f0ff;"><code>// C Example: Buffer Overflow', 
                '<pre><code class="language-c">// C Example: Buffer Overflow'
            )
            
        # Replace all other generic code blocks with Rust syntax
        original = re.sub(
            r'<pre[^>]*><code>',
            r'<pre><code class="language-rust">',
            original
        )
        
        if original != lesson.explanation_html:
            lesson.explanation_html = original
            updated = True
            
    if updated:
        lesson.save()
        print(f"Applied syntax highlighting classes to: {lesson.title}")

print("Syntax highlighting upgrade complete.")
