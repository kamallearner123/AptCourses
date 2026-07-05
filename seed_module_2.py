import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Course, Module, Lesson
from hide_mcq_answers_v2 import transform_mcqs_global
from highlight_abbreviations import highlight_text

course = Course.objects.get(title="Rust on STM32")
module = Module.objects.get(course=course, order=2) # Module 2: Rust Fundamentals

def process_and_save(lesson, exp, cha, ass, mcq):
    lesson.explanation_html = highlight_text(exp)
    lesson.challenges_html = highlight_text(cha)
    lesson.assignments_html = highlight_text(ass)
    lesson.mcqs_html = highlight_text(transform_mcqs_global(mcq))
    lesson.save()

# ==========================================
# M2.1: Variables & Data Types
# ==========================================
l1 = Lesson.objects.get(module=module, order=1)
exp1 = """
<img src="/static/images/comic_m2_l1.png" alt="Variables Comic" style="width: 100%; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid rgba(0,240,255,0.3);">
<h2>1. Strict Sizing in Embedded Systems</h2>
<p>In high-level languages like Python, an integer dynamically scales its memory usage. In embedded Rust, a microcontroller like the STM32F401RE has exactly 96KB of SRAM. You cannot afford dynamic scaling. Rust forces you to declare the exact bit-width of your integers.</p>
<pre><code class="language-rust">let sensor_value: u8 = 255; // 1 byte, Max 255
let motor_speed: u16 = 65000; // 2 bytes, Max 65535
let system_time: u32 = 4000000000; // 4 bytes
</code></pre>

<h2>2. Mutability is Explicit</h2>
<p>By default, variables in Rust are immutable. This is incredibly powerful for embedded state machines. If a calibration constant should never change after boot, Rust enforces it at compile-time.</p>
<pre><code class="language-rust">let calibration_offset = 42; // Immutable
// calibration_offset = 50; // ERROR: Cannot assign twice to immutable variable

let mut error_count = 0; // Mutable
error_count += 1; // OK
</code></pre>
"""
cha1 = """
<ol>
    <li><strong>Scenario Challenge 1:</strong> You are reading an ADC (Analog-to-Digital Converter) that outputs a 12-bit value. Which Rust integer type is the most memory-efficient choice to store this?</li>
    <li><strong>Scenario Challenge 2:</strong> Why is `let mut` safer for firmware than C's approach where variables are mutable by default?</li>
    <li><strong>Scenario Challenge 3:</strong> You need to track the uptime of a device in milliseconds. Why would `u16` be a disastrous choice for this variable?</li>
    <li><strong>Scenario Challenge 4:</strong> What happens at compile time if you try to assign `256` to a `u8` variable?</li>
    <li><strong>Scenario Challenge 5:</strong> Write out the Rust declaration for a constant float value representing Pi (3.14159) using 32-bit precision.</li>
</ol>
"""
ass1 = """
<ol>
    <li><strong>Type Architect:</strong> Design a `struct` called `SensorData` containing a 16-bit unsigned temperature, an 8-bit unsigned humidity, and a 32-bit signed altitude. Calculate the total byte size.</li>
    <li><strong>Overflow Analysis:</strong> Calculate exactly how long (in days) a `u32` millisecond counter can run before wrapping around to 0.</li>
</ol>
"""
mcq1 = """
<ol>
    <li><strong>MCQ 1:</strong> What is the default mutability of a variable declared with `let x = 5;`? <br><em>(A) Mutable (B) Immutable (C) Volatile</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 2:</strong> Which integer type requires 2 bytes of SRAM? <br><em>(A) u8 (B) u16 (C) u32</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 3:</strong> What is the maximum value a `u8` can hold? <br><em>(A) 127 (B) 255 (C) 256</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 4:</strong> True or False: Rust allows implicit type conversion (e.g., adding a `u8` directly to a `u16` without casting). <br><strong>Answer: False</strong></li>
    <li><strong>MCQ 5:</strong> Which keyword is used to make a variable modifiable? <br><em>(A) mod (B) var (C) mut</em><br><strong>Answer: C</strong></li>
</ol>
"""
process_and_save(l1, exp1, cha1, ass1, mcq1)

# ==========================================
# M2.2: Ownership & Borrowing
# ==========================================
l2 = Lesson.objects.get(module=module, order=2)
exp2 = """
<img src="/static/images/comic_m2_l2.png" alt="Ownership Comic" style="width: 100%; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid rgba(255,0,127,0.3);">
<h2>1. The Holy Grail of Safe Firmware</h2>
<p>In C, passing pointers around often leads to Data Races (two interrupts modifying the same buffer) or Dangling Pointers. Rust solves this via the Ownership model, checked strictly by the Compiler.</p>
<ul>
    <li>Each value has a single "owner".</li>
    <li>When the owner goes out of scope, the memory is safely dropped.</li>
</ul>

<h2>2. Borrowing Rules (The Referee)</h2>
<p>You can "borrow" access to data instead of taking ownership. But there are strict rules:</p>
<pre><code class="language-rust">let mut uart_buffer = [0u8; 64];

// Rule 1: You can have ANY number of immutable references (reads).
let reader1 = &uart_buffer;
let reader2 = &uart_buffer;

// Rule 2: You can have EXACTLY ONE mutable reference (write) at a time.
// let writer = &mut uart_buffer; // ERROR: Cannot borrow as mutable because it is already borrowed as immutable.
</code></pre>
<p>This single rule absolutely prevents Data Races at compile time. It is mathematically impossible to compile an STM32 firmware in safe Rust that has a data race.</p>
"""
cha2 = """
<ol>
    <li><strong>Scenario Challenge 1:</strong> An interrupt tries to write to a global buffer while the main loop is reading it. How does Rust's borrowing rules prevent this?</li>
    <li><strong>Scenario Challenge 2:</strong> Why can you have 100 immutable references `&T`, but only 1 mutable reference `&mut T`?</li>
    <li><strong>Scenario Challenge 3:</strong> Explain what "dropping" means when a variable's owner goes out of scope.</li>
</ol>
"""
ass2 = """
<ol>
    <li><strong>Ownership Trace:</strong> Write a small function that takes a `String` (heap allocated) and drops it. Explain why attempting to `println!()` that string back in `main()` causes a compile error.</li>
</ol>
"""
mcq2 = """
<ol>
    <li><strong>MCQ 1:</strong> How many mutable references to a specific piece of data are allowed in the same scope? <br><em>(A) 1 (B) 2 (C) Unlimited</em><br><strong>Answer: A</strong></li>
    <li><strong>MCQ 2:</strong> What happens when a variable's owner goes out of scope? <br><em>(A) Garbage collection (B) Memory leak (C) Memory is dropped/freed</em><br><strong>Answer: C</strong></li>
    <li><strong>MCQ 3:</strong> Which symbol is used to create an immutable borrow? <br><em>(A) * (B) & (C) mut</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 4:</strong> True or False: Rust uses a Garbage Collector to manage ownership. <br><strong>Answer: False</strong></li>
    <li><strong>MCQ 5:</strong> What specific class of bugs does the single-mutable-borrow rule prevent? <br><em>(A) Stack Overflow (B) Data Races (C) Off-by-one errors</em><br><strong>Answer: B</strong></li>
</ol>
"""
process_and_save(l2, exp2, cha2, ass2, mcq2)

# ==========================================
# M2.3: Enums & Pattern Matching
# ==========================================
l3 = Lesson.objects.get(module=module, order=3)
exp3 = """
<img src="/static/images/comic_m2_l3.png" alt="Enums Comic" style="width: 100%; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid rgba(0,240,255,0.3);">
<h2>1. Beyond C-Style Enums</h2>
<p>In C, an enum is just an integer under the hood. In Rust, Enums are Algebraic Data Types—they can carry distinct payloads!</p>
<pre><code class="language-rust">enum SensorState {
    Offline,
    Calibrating,
    Active(f32), // Payload: The actual temperature!
    Error(u8),   // Payload: The error code!
}
</code></pre>

<h2>2. The Exhaustive `match`</h2>
<p>When you read a sensor, the compiler forces you to handle every possible state via the `match` control flow. No unhandled edge cases!</p>
<pre><code class="language-rust">let state = SensorState::Active(24.5);

match state {
    SensorState::Offline => turn_on_red_led(),
    SensorState::Calibrating => turn_on_yellow_led(),
    SensorState::Active(temp) => send_to_uart(temp),
    SensorState::Error(code) => reset_sensor(code),
}
</code></pre>
"""
cha3 = """
<ol>
    <li><strong>Scenario Challenge 1:</strong> You are designing a protocol parser. Design an Enum called `Packet` that can be either a `Ping`, a `Data` packet containing a `[u8; 4]` array, or an `Ack` packet containing a `u16` ID.</li>
    <li><strong>Scenario Challenge 2:</strong> Why is `match` safer than a C-style `switch` statement regarding edge cases?</li>
    <li><strong>Scenario Challenge 3:</strong> What happens if you forget to handle the `Error` variant in a `match` block?</li>
</ol>
"""
ass3 = """
<ol>
    <li><strong>Traffic Light State Machine:</strong> Write a Rust Enum representing Traffic Light states. Write a function that takes a state and uses a `match` block to return the duration in seconds that state should hold.</li>
</ol>
"""
mcq3 = """
<ol>
    <li><strong>MCQ 1:</strong> Can Rust enums hold different types of data payloads in different variants? <br><em>(A) Yes (B) No</em><br><strong>Answer: A</strong></li>
    <li><strong>MCQ 2:</strong> What compiler feature ensures all Enum variants are handled in a match statement? <br><em>(A) Exhaustive checking (B) Pattern inferencing (C) Drop checking</em><br><strong>Answer: A</strong></li>
    <li><strong>MCQ 3:</strong> What keyword extracts the payload from an enum variant during a match? <br><em>(A) extract (B) let (C) It is extracted directly as a variable in the match arm pattern</em><br><strong>Answer: C</strong></li>
    <li><strong>MCQ 4:</strong> True or False: Rust Enums are essentially just C-Unions wrapped in a struct. <br><strong>Answer: True</strong> (Technically, they are Tagged Unions).</li>
    <li><strong>MCQ 5:</strong> What wildcard character is used to match "everything else" in a match block? <br><em>(A) * (B) _ (C) default</em><br><strong>Answer: B</strong></li>
</ol>
"""
process_and_save(l3, exp3, cha3, ass3, mcq3)


# ==========================================
# M2.4: Traits & Lifetimes
# ==========================================
l4 = Lesson.objects.get(module=module, order=4)
exp4 = """
<img src="/static/images/comic_m2_l4.png" alt="Lifetimes Comic" style="width: 100%; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid rgba(255,0,127,0.3);">
<h2>1. Traits: Shared Behavior</h2>
<p>Rust does not have classes or inheritance. Instead, it uses <strong>Traits</strong>. A Trait defines functionality a type must provide. This is heavily used in the embedded HAL (Hardware Abstraction Layer).</p>
<pre><code class="language-rust">pub trait OutputPin {
    fn set_high(&mut self);
    fn set_low(&mut self);
}

// Now we can write drivers that accept ANY pin, whether it's on an STM32 or an NRF52!
fn blink_twice(pin: &mut impl OutputPin) {
    pin.set_high();
    // wait...
    pin.set_low();
}
</code></pre>

<h2>2. Lifetimes: The Invisible Tether</h2>
<p>When you pass a reference around, the compiler tracks its "Lifetime" (denoted by `'a`). This ensures that a reference never outlives the data it points to, completely eliminating Dangling Pointers.</p>
<pre><code class="language-rust">struct DmaBuffer<'a> {
    data: &'a [u8], // The struct cannot outlive the slice it references!
}
</code></pre>
"""
cha4 = """
<ol>
    <li><strong>Scenario Challenge 1:</strong> Why are Traits better suited for Embedded Systems HALs than traditional Object-Oriented Class Inheritance?</li>
    <li><strong>Scenario Challenge 2:</strong> A DMA controller needs a reference to a memory buffer. How does a lifetime `'a` prevent the DMA from reading memory after the buffer function returns?</li>
    <li><strong>Scenario Challenge 3:</strong> What does `impl Trait` mean in a function parameter?</li>
</ol>
"""
ass4 = """
<ol>
    <li><strong>Trait Definition:</strong> Define a `TemperatureSensor` trait with a function `read_temp` that returns an `f32`.</li>
    <li><strong>Lifetime Tracking:</strong> Write a struct `SpiDevice<'a>` that holds a reference to a configuration array. Ensure the lifetime syntax is correct.</li>
</ol>
"""
mcq4 = """
<ol>
    <li><strong>MCQ 1:</strong> Does Rust support traditional Class Inheritance (like `class Car extends Vehicle`)? <br><em>(A) Yes (B) No</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 2:</strong> What is the Rust equivalent to an Interface in Java or C#? <br><em>(A) Struct (B) Enum (C) Trait</em><br><strong>Answer: C</strong></li>
    <li><strong>MCQ 3:</strong> What syntax denotes a specific explicit lifetime? <br><em>(A) $a (B) 'a (C) &a</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 4:</strong> What bug do Lifetimes mathematically prevent? <br><em>(A) Null pointer exceptions (B) Dangling Pointers (C) Integer Overflow</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 5:</strong> What does the `embedded-hal` crate primarily consist of? <br><em>(A) C-bindings (B) Pre-compiled binaries (C) Traits defining standard hardware behaviors</em><br><strong>Answer: C</strong></li>
</ol>
"""
process_and_save(l4, exp4, cha4, ass4, mcq4)

print("Module 2 fully seeded with comics, content, and parsed assessments!")
