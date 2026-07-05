import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Category, Course, Module, Lesson

# 1. Create Category
category, _ = Category.objects.get_or_create(
    name="Embedded Systems",
    defaults={"slug": "embedded-systems"}
)

# 2. Create Course
course, _ = Course.objects.update_or_create(
    title="Rust on STM32",
    defaults={
        "category": category,
        "skill_level": "Intermediate",
        "duration": "40 hours",
        "price": 49.99,
        "tags": "Rust, STM32, Embedded, ARM, Bare-Metal",
        "permission_type": "public",
        "overview": "A complete, hands-on, project-driven course teaching you how to write safe, concurrent, and reliable embedded firmware for ARM Cortex-M microcontrollers using Rust.",
        "syllabus": "Covers 20 modules from basic Rust setup, GPIO, UART, I2C, SPI, Interrupts, up to a full Capstone Data Logger project.",
        "outcomes": "Write safe bare-metal code, interface with all standard peripherals, use interrupts safely, and master the no_std ecosystem.",
        "prerequisites": "Basic C/C++ knowledge, basic electronics understanding. No prior Rust required.",
        "status": "published"
    }
)

# 3. Define the 20 Modules and their Lessons
course_structure = {
    1: ("Module 1: Introduction", ["M1.1: Why Rust for STM32", "M1.2: STM32 Families Overview", "M1.3: Hardware Safety Basics"]),
    2: ("Module 2: Rust Fundamentals", ["M2.1: Variables & Data Types", "M2.2: Ownership & Borrowing", "M2.3: Enums & Pattern Matching", "M2.4: Traits & Lifetimes"]),
    3: ("Module 3: Embedded Rust Mindset", ["M3.1: The no_std environment", "M3.2: Deterministic Behavior", "M3.3: Panic Handling"]),
    4: ("Module 4: STM32 Basics", ["M4.1: Memory Mapping", "M4.2: Reading Datasheets", "M4.3: Reset and Startup Flow"]),
    5: ("Module 5: Setup and First Build", ["M5.1: Rust Embedded Toolchain", "M5.2: Configuring Cargo", "M5.3: Common Setup Mistakes"]),
    6: ("Module 6: First Embedded Project", ["M6.1: Project Structure", "M6.2: Blink LED", "M6.3: Flashing via probe-rs"]),
    7: ("Module 7: GPIO and Digital I/O", ["M7.1: Input/Output Pins", "M7.2: Debouncing Buttons"]),
    8: ("Module 8: Timing and Delays", ["M8.1: SysTick", "M8.2: Non-blocking Execution"]),
    9: ("Module 9: UART Serial Communication", ["M9.1: UART Theory", "M9.2: Terminal Logging", "M9.3: Reading Serial Commands"]),
    10: ("Module 10: I2C", ["M10.1: I2C Theory", "M10.2: Reading I2C Sensors"]),
    11: ("Module 11: SPI", ["M11.1: SPI Theory", "M11.2: SPI Displays"]),
    12: ("Module 12: ADC and Analog Input", ["M12.1: Analog Sampling", "M12.2: Potentiometer Scaling"]),
    13: ("Module 13: PWM", ["M13.1: Duty Cycles", "M13.2: Fading LEDs"]),
    14: ("Module 14: Interrupts and Events", ["M14.1: NVIC Overview", "M14.2: Safe Shared State", "M14.3: Timer Interrupts"]),
    15: ("Module 15: Embedded Rust Ecosystem", ["M15.1: cortex-m crate", "M15.2: PACs vs HALs", "M15.3: Logging with defmt"]),
    16: ("Module 16: Memory and Reliability", ["M16.1: Stack vs Static Memory", "M16.2: Defensive Design"]),
    17: ("Module 17: Debugging and Troubleshooting", ["M17.1: GDB & probe-rs", "M17.2: Deciphering Errors", "M17.3: Clock Config Issues"]),
    18: ("Module 18: Real Projects", ["M18.1: Serial Command Interface", "M18.2: I2C Environment Monitor", "M18.3: Smart Controller"]),
    19: ("Module 19: Advanced Topics", ["M19.1: Low-power Modes", "M19.2: Cooperative Multitasking", "M19.3: HIL Testing"]),
    20: ("Module 20: Capstone Project", ["M20.1: Smart Sensor Dashboard", "M20.2: System Integration", "M20.3: AI Grading"]),
}

# 4. Generate the structure in the DB
print(f"Seeding structure for '{course.title}'...")
for mod_order, (mod_title, lessons) in course_structure.items():
    module, _ = Module.objects.update_or_create(
        course=course,
        title=mod_title,
        defaults={"order": mod_order}
    )
    
    for les_idx, les_title in enumerate(lessons):
        # We add some placeholder text so the frontend renders beautifully.
        placeholder = f"<p>Detailed content, cargo examples, 10 Challenges, 3 Assignments, and 10 MCQs for <strong>{les_title}</strong> will be populated in Phase 2.</p>"
        Lesson.objects.update_or_create(
            module=module,
            title=les_title,
            defaults={
                "order": les_idx + 1,
                "explanation_html": f"<h3>{les_title}</h3>{placeholder}",
                "challenges_html": "<ul><li>Challenge 1</li><li>Challenge 2</li><li>... 8 more</li></ul>",
                "assignments_html": "<ul><li>Assignment 1</li><li>... 2 more</li></ul>",
                "mcqs_html": "<ul><li>MCQ 1</li><li>MCQ 2</li><li>... 8 more</li></ul>",
            }
        )
        
print("Successfully generated 20 Modules and all Lessons!")
