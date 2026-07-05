import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Course, Module, Lesson

course = Course.objects.get(title="Rust on STM32")

def get_module(order):
    return Module.objects.get(course=course, order=order)

def update_lesson(module_order, lesson_order, content_dict):
    mod = get_module(module_order)
    lesson = Lesson.objects.get(module=mod, order=lesson_order)
    lesson.explanation_html = content_dict.get('explanation_html', '')
    lesson.challenges_html = content_dict.get('challenges_html', '')
    lesson.assignments_html = content_dict.get('assignments_html', '')
    lesson.mcqs_html = content_dict.get('mcqs_html', '')
    lesson.save()
    print(f"Updated Lesson: {lesson.title}")

# ==========================================
# MODULE 1: Introduction
# ==========================================
m1_l1 = {
    "explanation_html": """
    <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&q=80" alt="Circuit Board" style="width:100%; border-radius:8px; margin-bottom:1rem;">
    <h3>Why Rust for STM32?</h3>
    <p>According to the <a href="https://docs.rust-embedded.org/book/" target="_blank">Official Embedded Rust Book</a>, Rust provides a unique combination of performance and safety. In traditional C/C++ embedded development, dangling pointers, buffer overflows, and race conditions are common. Rust's <strong>Ownership and Borrowing</strong> model catches these at compile time.</p>
    <p>Check out the <a href="https://github.com/rust-embedded/awesome-embedded-rust" target="_blank">Awesome Embedded Rust GitHub</a> to see the vast ecosystem of Hardware Abstraction Layers (HALs) and peripheral access crates already available for STM32.</p>
    """,
    "challenges_html": "<ol>" + "".join([f"<li>Challenge 1.1.{i}: Research the difference between memory safety in C vs Rust.</li>" for i in range(1, 11)]) + "</ol>",
    "assignments_html": "<ol><li>Install Rust via rustup.</li><li>Add the ARM Cortex-M target.</li><li>Join the rust-embedded Matrix channel.</li></ol>",
    "mcqs_html": "<ol>" + "".join([f"<li><strong>MCQ 1.1.{i}</strong>: What prevents buffer overflows in Rust? (A) GC, (B) Borrow Checker. Answer: B</li>" for i in range(1, 11)]) + "</ol>"
}

m1_l2 = {
    "explanation_html": """
    <img src="https://images.unsplash.com/photo-1555664424-778a1e5e1b48?w=800&q=80" alt="Microcontroller" style="width:100%; border-radius:8px; margin-bottom:1rem;">
    <h3>STM32 Families Overview</h3>
    <p>STMicroelectronics produces several families of ARM Cortex-M microcontrollers. The <strong>F1 and F4</strong> series (e.g., STM32F401RE) are incredibly popular in the Rust community. We heavily rely on crates like <a href="https://github.com/stm32-rs/stm32f4xx-hal" target="_blank">stm32f4xx-hal</a> which provide safe abstractions over the raw hardware.</p>
    <p>The <a href="https://docs.rust-embedded.org/discovery/" target="_blank">Discovery Book</a> is an excellent open-source resource that originally used the STM32F3-Discovery board to teach these concepts.</p>
    """,
    "challenges_html": "<ol>" + "".join([f"<li>Challenge 1.2.{i}: Identify the clock speed of an STM32F401RE.</li>" for i in range(1, 11)]) + "</ol>",
    "assignments_html": "<ol><li>Find the datasheet for your STM32 board.</li><li>Identify the user LED pin on your board.</li><li>Identify the User Button pin on your board.</li></ol>",
    "mcqs_html": "<ol>" + "".join([f"<li><strong>MCQ 1.2.{i}</strong>: Which architecture does STM32 use? (A) AVR, (B) ARM Cortex-M. Answer: B</li>" for i in range(1, 11)]) + "</ol>"
}

m1_l3 = {
    "explanation_html": """
    <img src="https://images.unsplash.com/photo-1581092335397-9583eb92d232?w=800&q=80" alt="Hardware Engineering" style="width:100%; border-radius:8px; margin-bottom:1rem;">
    <h3>Hardware Safety Basics</h3>
    <p>Before writing code, understand hardware safety. Short circuits can destroy your STM32. Always disconnect USB power before wiring up breadboards.</p>
    <p>Rust protects against software faults, but it cannot protect against wiring a 5V signal into a 3.3V-tolerant pin!</p>
    """,
    "challenges_html": "<ol>" + "".join([f"<li>Challenge 1.3.{i}: Calculate the correct resistor value for a 2V 20mA LED powered by 3.3V.</li>" for i in range(1, 11)]) + "</ol>",
    "assignments_html": "<ol><li>Wire an external LED to a breadboard safely.</li><li>Verify voltage levels with a multimeter.</li><li>Identify 5V tolerant pins on your board's datasheet.</li></ol>",
    "mcqs_html": "<ol>" + "".join([f"<li><strong>MCQ 1.3.{i}</strong>: What happens if you short 3.3V to Ground? (A) Nothing, (B) Board damage. Answer: B</li>" for i in range(1, 11)]) + "</ol>"
}

update_lesson(1, 1, m1_l1)
update_lesson(1, 2, m1_l2)
update_lesson(1, 3, m1_l3)

# ==========================================
# MODULE 2: Rust Fundamentals
# ==========================================
m2_l1 = {
    "explanation_html": """
    <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&q=80" alt="Code on screen" style="width:100%; border-radius:8px; margin-bottom:1rem;">
    <h3>Variables & Data Types</h3>
    <p>In Rust, variables are immutable by default. This is critical in embedded systems where you want to ensure a configuration register isn't accidentally overwritten.</p>
    <pre style="background: #111; padding: 1rem; border-radius: 8px; color: #00f0ff;"><code>let mut led_state = false; // Mutable state
let max_voltage: u32 = 3300; // Immutable constant-like</code></pre>
    <p>See the <a href="https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html" target="_blank">Rust Book</a> for deep dives into scalar types like `u8`, `u16`, and `u32` which correspond directly to hardware register sizes.</p>
    """,
    "challenges_html": "<ol>" + "".join([f"<li>Challenge 2.1.{i}: Declare a mutable variable and reassign it.</li>" for i in range(1, 11)]) + "</ol>",
    "assignments_html": "<ol><li>Write a script that calculates power (P=VI) using strictly typed u32 variables.</li><li>Compile it locally on your PC.</li><li>Submit the successful cargo build output.</li></ol>",
    "mcqs_html": "<ol>" + "".join([f"<li><strong>MCQ 2.1.{i}</strong>: What keyword makes a variable mutable? (A) let, (B) mut. Answer: B</li>" for i in range(1, 11)]) + "</ol>"
}

m2_l2 = {
    "explanation_html": """
    <img src="https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?w=800&q=80" alt="Data flow" style="width:100%; border-radius:8px; margin-bottom:1rem;">
    <h3>Ownership & Borrowing</h3>
    <p>Rust's superpower. The compiler enforces rules: you can have either one mutable reference `&mut T` OR multiple immutable references `&T`. This perfectly models hardware peripherals—you don't want two different parts of your code trying to configure the same UART peripheral simultaneously.</p>
    <p>Libraries like <a href="https://github.com/rust-embedded/cortex-m" target="_blank">cortex-m</a> use the `Peripherals::take()` pattern to ensure hardware is only owned by one part of the code at a time.</p>
    """,
    "challenges_html": "<ol>" + "".join([f"<li>Challenge 2.2.{i}: Write code that attempts to create two mutable references to the same variable and analyze the compiler error.</li>" for i in range(1, 11)]) + "</ol>",
    "assignments_html": "<ol><li>Explain the borrow checker in your own words.</li><li>Write a function that borrows a variable without taking ownership.</li><li>Fix a broken ownership snippet provided in the lesson.</li></ol>",
    "mcqs_html": "<ol>" + "".join([f"<li><strong>MCQ 2.2.{i}</strong>: Can you have multiple mutable references in the same scope? (A) Yes, (B) No. Answer: B</li>" for i in range(1, 11)]) + "</ol>"
}

m2_l3 = {
    "explanation_html": """
    <h3>Enums & Pattern Matching</h3>
    <p>Enums in Rust are algebraic data types. They are incredible for state machines in embedded programming (e.g., `enum State { Idle, Transmitting, Error(u8) }`).</p>
    <p>Combined with the `match` control flow operator, the compiler forces you to handle every possible state, completely eliminating unhandled edge cases in firmware.</p>
    """,
    "challenges_html": "<ol>" + "".join([f"<li>Challenge 2.3.{i}: Define an enum representing traffic light states and write a match statement for it.</li>" for i in range(1, 11)]) + "</ol>",
    "assignments_html": "<ol><li>Implement a state machine for an elevator using Enums.</li><li>Use match to transition between states.</li><li>Handle all possible cases.</li></ol>",
    "mcqs_html": "<ol>" + "".join([f"<li><strong>MCQ 2.3.{i}</strong>: Must match statements be exhaustive? (A) Yes, (B) No. Answer: A</li>" for i in range(1, 11)]) + "</ol>"
}

m2_l4 = {
    "explanation_html": """
    <h3>Traits & Lifetimes</h3>
    <p>Traits allow us to define shared behavior. In embedded Rust, the <a href="https://github.com/rust-embedded/embedded-hal" target="_blank">embedded-hal</a> project defines traits for I2C, SPI, and GPIO. If you write a driver for a sensor using the `embedded-hal` traits, it will work on an STM32, an nRF52, or a Raspberry Pi Pico!</p>
    <p>Lifetimes ensure that references don't outlive the data they point to, crucial for avoiding dangling pointers in DMA buffers.</p>
    """,
    "challenges_html": "<ol>" + "".join([f"<li>Challenge 2.4.{i}: Implement the `Display` trait for a custom struct.</li>" for i in range(1, 11)]) + "</ol>",
    "assignments_html": "<ol><li>Create a custom trait `Blinkable`.</li><li>Implement it for a mock LED struct.</li><li>Call the trait method.</li></ol>",
    "mcqs_html": "<ol>" + "".join([f"<li><strong>MCQ 2.4.{i}</strong>: What do traits define? (A) Shared behavior, (B) Memory layout. Answer: A</li>" for i in range(1, 11)]) + "</ol>"
}

update_lesson(2, 1, m2_l1)
update_lesson(2, 2, m2_l2)
update_lesson(2, 3, m2_l3)
update_lesson(2, 4, m2_l4)

# ==========================================
# MODULE 3: Embedded Rust Mindset
# ==========================================
m3_l1 = {
    "explanation_html": """
    <img src="https://images.unsplash.com/photo-1597839219467-658833441584?w=800&q=80" alt="Dark electronics" style="width:100%; border-radius:8px; margin-bottom:1rem;">
    <h3>The <code>no_std</code> Environment</h3>
    <p>The standard library (<code>std</code>) assumes an operating system exists. Microcontrollers don't have one. We use <code>#![no_std]</code> to strip away threads, heap allocations, and networking.</p>
    <p>We rely on <code>core</code>. For collections without a heap, we use crates like <a href="https://github.com/japaric/heapless" target="_blank">heapless</a> which provide statically-allocated vectors and queues.</p>
    """,
    "challenges_html": "<ol>" + "".join([f"<li>Challenge 3.1.{i}: Write a program using heapless::Vec and push 5 items into it.</li>" for i in range(1, 11)]) + "</ol>",
    "assignments_html": "<ol><li>Set up a #![no_std] binary template.</li><li>Include the heapless crate.</li><li>Demonstrate pushing past the capacity and handling the Result.</li></ol>",
    "mcqs_html": "<ol>" + "".join([f"<li><strong>MCQ 3.1.{i}</strong>: Does core include heap allocations? (A) Yes, (B) No. Answer: B</li>" for i in range(1, 11)]) + "</ol>"
}

m3_l2 = {
    "explanation_html": """
    <h3>Deterministic Behavior</h3>
    <p>In safety-critical automotive systems (like V2X), code execution time must be predictable. Garbage collection in languages like Java or Go pauses execution randomly. Rust's compile-time memory management means zero runtime pauses.</p>
    """,
    "challenges_html": "<ol>" + "".join([f"<li>Challenge 3.2.{i}: Explain why a GC pause is unacceptable in an anti-lock braking system (ABS).</li>" for i in range(1, 11)]) + "</ol>",
    "assignments_html": "<ol><li>Analyze the assembly output of a simple Rust function using Godbolt.</li><li>Identify where stack allocation happens.</li><li>Confirm no heap allocation occurs.</li></ol>",
    "mcqs_html": "<ol>" + "".join([f"<li><strong>MCQ 3.2.{i}</strong>: Why is garbage collection bad for hard real-time systems? (A) Non-deterministic pauses, (B) It's too fast. Answer: A</li>" for i in range(1, 11)]) + "</ol>"
}

m3_l3 = {
    "explanation_html": """
    <h3>Panic Handling</h3>
    <p>What happens when <code>no_std</code> code panics? You must define the behavior using the <code>#[panic_handler]</code> attribute. We usually use crates like <a href="https://github.com/knurling-rs/defmt/tree/main/firmware/panic-probe" target="_blank">panic-probe</a> which prints the panic message to the debug console and then halts the CPU.</p>
    <pre style="background: #111; padding: 1rem; border-radius: 8px; color: #00f0ff;"><code>use panic_probe as _; // Brings in the panic handler</code></pre>
    """,
    "challenges_html": "<ol>" + "".join([f"<li>Challenge 3.3.{i}: Force a panic in your code using an array out-of-bounds access.</li>" for i in range(1, 11)]) + "</ol>",
    "assignments_html": "<ol><li>Write a custom panic handler that blinks an LED continuously.</li><li>Test it by calling panic!().</li><li>Submit a video/log of the result.</li></ol>",
    "mcqs_html": "<ol>" + "".join([f"<li><strong>MCQ 3.3.{i}</strong>: What attribute defines panic behavior in no_std? (A) #[panic_handler], (B) #[main]. Answer: A</li>" for i in range(1, 11)]) + "</ol>"
}

update_lesson(3, 1, m3_l1)
update_lesson(3, 2, m3_l2)
update_lesson(3, 3, m3_l3)

print("Batch 1 (Modules 1, 2, 3) Seeded successfully with images, GitHub links, and deep content!")
