import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Course, Category

category, created = Category.objects.get_or_create(
    name="Embedded Systems",
    defaults={"slug": "embedded-systems"}
)

course, course_created = Course.objects.update_or_create(
    title="Rust on STM32",
    defaults={
        "category": category,
        "skill_level": "Intermediate",
        "duration": "20 hours",
        "price": 39.99,
        "tags": "Rust, STM32, Embedded, RTOS",
        "permission_type": "public",
        "overview": "Learn how to program STM32 microcontrollers using the Rust programming language for safe and concurrent embedded systems.",
        "syllabus": "1. Introduction to Rust for Embedded Systems (no_std)\n2. Ownership, Borrowing, & Memory Safety\n3. Setting up the STM32 Toolchain (probe-run, openocd)\n4. PACs vs Hardware Abstraction Layers (HAL)\n5. GPIO, Interrupts, and Exception Handling\n6. Serial Communication (UART, I2C, SPI)\n7. Timers, PWM, and ADC\n8. Direct Memory Access (DMA) in Rust\n9. Concurrency with RTIC (Real-Time Interrupt-driven Concurrency)\n10. Power Management & Low-Power Modes\n11. Final Project: Building a complete Sensor Data Logger",
        "outcomes": "• Master Rust's ownership model in a resource-constrained environment.\n• Configure and debug STM32 MCUs using modern Rust tooling.\n• Write safe, bare-metal drivers for SPI, I2C, and UART peripherals.\n• Build concurrent embedded applications using the RTIC framework.\n• Eliminate data races and undefined behavior typically found in C/C++ firmware.",
        "prerequisites": "• Basic understanding of C/C++ and microcontroller architecture.\n• Familiarity with basic electronics and hardware interfacing.\n• No prior Rust experience required, but general programming knowledge is essential.",
        "status": "published"
    }
)

if course_created:
    print(f"Successfully created course: '{course.title}'")
else:
    print(f"Successfully updated course: '{course.title}'")
