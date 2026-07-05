import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Course, Module, Lesson
from hide_mcq_answers_v2 import transform_mcqs_global
from highlight_abbreviations import highlight_text

course = Course.objects.get(title="Rust on STM32")
module = Module.objects.get(course=course, order=3)

def process_and_save(lesson, exp, cha, ass, mcq):
    lesson.explanation_html = highlight_text(exp)
    lesson.challenges_html = highlight_text(cha)
    lesson.assignments_html = highlight_text(ass)
    lesson.mcqs_html = highlight_text(transform_mcqs_global(mcq))
    lesson.save()

# ==========================================
# M3.1: The no_std environment
# ==========================================
l1 = Lesson.objects.get(module=module, order=1)
exp1 = """
<img src="/static/images/comic_m3_l1.png" alt="no_std Comic" style="width: 100%; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid rgba(0,240,255,0.3);">

<h2>1. A Simple Explanation: `#![no_std]`</h2>
<p>When you write code for a normal computer, you have access to a giant toolbox called the "Standard Library" (or <code>std</code>). This toolbox lets you do things like open files, connect to the internet, or ask the Operating System for memory (using the heap). But an STM32 microcontroller is a tiny island—it has no Operating System!</p>
<p>If you try to bring the giant <code>std</code> toolbox to the island, it will sink. So, in embedded Rust, we put a label at the very top of our code: <code>#![no_std]</code>. This tells the compiler, "Leave the heavy standard library behind, I only need the essentials (called <code>core</code>)."</p>

<h2>2. Why It Matters</h2>
<p>Without `#![no_std]`, your firmware literally wouldn't compile for an STM32 because the compiler would look for an underlying Linux or Windows OS that doesn't exist. By removing the standard library, you guarantee that your code will run directly on the "bare metal" of the silicon.</p>

<h2>3. Small Code Example</h2>
<pre><code class="language-rust">// This line MUST be at the very top of your main.rs file
#![no_std]
#![no_main] // We also don't use standard OS 'main' execution!

use core::panic::PanicInfo;

// We have to define our own panic handler since we don't have std!
#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}
</code></pre>

<h2>4. Embedded Firmware Example</h2>
<p>Because you don't have `std`, you can't use standard dynamically sized types like `String` or `Vec`. Instead, you use fixed-size arrays from the `core` library.</p>
<pre><code class="language-rust">#![no_std]

// We CANNOT do this:
// let my_text = String::from("Hello"); // ERROR: String is part of std!

// We MUST do this instead:
let my_text: [u8; 5] = [b'H', b'e', b'l', b'l', b'o'];
</code></pre>

<h2>5. Recap</h2>
<p>`#![no_std]` strips away the heavy OS-dependent standard library. You use `core` instead. This means no heap allocations (no `String`, no `Vec`), ensuring your code is tiny and runs directly on the STM32 processor.</p>

<h2>6. Common Mistakes Beginners Make</h2>
<ul>
    <li>Trying to use `std::collections::HashMap` or `std::string::String` in an embedded project. The compiler will complain that `std` is missing.</li>
    <li>Forgetting to add `#![no_main]`. An OS looks for `main()`, but bare-metal hardware looks for a specific memory address called the Reset Vector!</li>
</ul>
"""
cha1 = """
<ol>
    <li><strong>Challenge 1:</strong> Explain in your own words why we cannot use `std::fs::File` to open a file on an STM32 microcontroller.</li>
    <li><strong>Challenge 2:</strong> What is the name of the lightweight, OS-independent library that Rust provides instead of `std`?</li>
</ol>
"""
ass1 = """
<p><strong>Assignment Idea:</strong> Create a new cargo project. Add `#![no_std]` to the top. Try to define a `Vec<u8>`. Paste the compiler error you receive explaining why `Vec` cannot be found.</p>
"""
mcq1 = """
<ol>
    <li><strong>MCQ 1:</strong> What does the `#![no_std]` macro do? <br><em>(A) Disables the Rust compiler (B) Disables the OS-dependent Standard Library (C) Disables memory safety</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 2:</strong> Which library do we use in `#![no_std]` environments for basic types and operations? <br><em>(A) std (B) core (C) alloc</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 3:</strong> Why can't you use `String` in a strict `#![no_std]` environment by default? <br><em>(A) It requires heap allocation (B) It is too slow (C) It only works on 64-bit systems</em><br><strong>Answer: A</strong></li>
    <li><strong>MCQ 4:</strong> True or False: An STM32 microcontroller has a built-in Linux operating system by default. <br><strong>Answer: False</strong></li>
    <li><strong>MCQ 5:</strong> What other macro is almost always paired with `#![no_std]` in firmware? <br><em>(A) #![no_main] (B) #![no_core] (C) #![fast_math]</em><br><strong>Answer: A</strong></li>
</ol>
"""
process_and_save(l1, exp1, cha1, ass1, mcq1)

# ==========================================
# M3.2: Deterministic Behavior
# ==========================================
l2 = Lesson.objects.get(module=module, order=2)
exp2 = """
<img src="/static/images/comic_m3_l2.png" alt="Deterministic Behavior Comic" style="width: 100%; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid rgba(255,0,127,0.3);">

<h2>1. A Simple Explanation: Determinism</h2>
<p>Imagine a robot trying to catch a ball. If the robot's brain gets distracted by checking its email (like a desktop computer OS does), it will pause for a few milliseconds and miss the ball entirely. This is <em>non-deterministic</em>.</p>
<p><strong>Deterministic Behavior</strong> means that if a piece of code takes exactly 14 microseconds to run today, it will take exactly 14 microseconds to run tomorrow, the next day, and forever. It never lags. It never gets distracted by a background OS update.</p>

<h2>2. Why It Matters</h2>
<p>In bare-metal embedded systems, timing is everything. If you are controlling an engine fuel injector, firing 5 milliseconds late could destroy the engine. Writing bare-metal `#![no_std]` Rust guarantees you have absolute, deterministic control over the processor's execution time.</p>

<h2>3. Small Code Example</h2>
<pre><code class="language-rust">// A completely deterministic delay loop
// Because there is no OS to preempt this thread, 
// we know exactly how many CPU cycles this takes.
fn delay_cycles(cycles: u32) {
    for _ in 0..cycles {
        // NOP (No Operation) instruction
        cortex_m::asm::nop(); 
    }
}
</code></pre>

<h2>4. Embedded Firmware Example</h2>
<p>When dealing with hardware interrupts, we need determinism to ensure we respond to physical events (like a button press or an incoming UART byte) immediately.</p>
<pre><code class="language-rust">#[interrupt]
fn USART1() {
    // This function will run IMMEDIATELY when a byte arrives.
    // There is no OS scheduler deciding to delay it.
    let byte = serial_port.read().unwrap();
    process(byte);
}
</code></pre>

<h2>5. Recap</h2>
<p>Determinism means predictable, consistent timing. Desktop computers are non-deterministic because their heavy Operating Systems constantly pause programs to do other things. Bare-metal STM32 firmware is deterministic because your code is the *only* thing running on the chip.</p>

<h2>6. Common Mistakes Beginners Make</h2>
<ul>
    <li>Assuming that code running on an STM32 will be slower than a PC. While the clock speed (e.g., 84MHz) is slower than a 4GHz PC, the STM32 can often respond to an external pin change <em>faster</em> than a PC because there is zero OS overhead!</li>
</ul>
"""
cha2 = """
<ol>
    <li><strong>Challenge 1:</strong> Give a real-world example (e.g., in automotive or medical devices) where non-deterministic lag could be catastrophic.</li>
    <li><strong>Challenge 2:</strong> Why does a Linux computer sometimes "freeze" for a second, whereas a bare-metal STM32 never does?</li>
</ol>
"""
ass2 = """
<p><strong>Assignment Idea:</strong> Research the concept of an RTOS (Real-Time Operating System). Write a 2-sentence summary of how an RTOS differs from a general-purpose OS like Windows regarding determinism.</p>
"""
mcq2 = """
<ol>
    <li><strong>MCQ 1:</strong> What does deterministic execution mean? <br><em>(A) The code runs as fast as possible (B) The code takes the exact same amount of time to run every time (C) The code uses AI to predict execution</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 2:</strong> Why is a desktop OS like Windows non-deterministic? <br><em>(A) The OS scheduler can pause your program at any time (B) The CPU is too fast (C) The memory is too large</em><br><strong>Answer: A</strong></li>
    <li><strong>MCQ 3:</strong> What instruction is often used to waste exactly one CPU cycle for precise delays? <br><em>(A) pause (B) wait (C) nop</em><br><strong>Answer: C</strong></li>
    <li><strong>MCQ 4:</strong> True or False: Bare-metal code can guarantee faster worst-case response times to hardware events than a standard desktop OS. <br><strong>Answer: True</strong></li>
    <li><strong>MCQ 5:</strong> Which application strictly requires deterministic behavior? <br><em>(A) Loading a webpage (B) Anti-lock braking systems (ABS) (C) Rendering a video</em><br><strong>Answer: B</strong></li>
</ol>
"""
process_and_save(l2, exp2, cha2, ass2, mcq2)


# ==========================================
# M3.3: Panic Handling
# ==========================================
l3 = Lesson.objects.get(module=module, order=3)
exp3 = """
<img src="/static/images/comic_m3_l3.png" alt="Panic Handling Comic" style="width: 100%; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid rgba(0,240,255,0.3);">

<h2>1. A Simple Explanation: Panic Handling</h2>
<p>In standard Rust, if your code hits a catastrophic, unrecoverable error (like trying to access the 10th item in a 3-item array), the program "panics." On a PC, the OS catches this panic, prints an error to your terminal, and safely closes the app.</p>
<p>On an STM32, there is no OS to catch you! If you panic, the processor has no idea what to do. It might just keep executing random garbage memory, which could literally cause a connected motor to catch fire. Therefore, in `#![no_std]`, Rust forces <em>you</em> to define the big red Emergency Stop button.</p>

<h2>2. Why It Matters</h2>
<p>Defining a `#[panic_handler]` is mandatory in `#![no_std]` Rust. It ensures that when the worst happens, you dictate a safe fail-state. Usually, this means halting the CPU completely or triggering a system reset.</p>

<h2>3. Small Code Example</h2>
<pre><code class="language-rust">#![no_std]
use core::panic::PanicInfo;
use cortex_m::asm;

// This function is called automatically if a panic occurs!
#[panic_handler]
fn safe_shutdown(info: &PanicInfo) -> ! {
    // 1. You would turn off all motors/heaters here.
    
    // 2. Halt the processor safely.
    loop {
        // Wait For Interrupt instruction puts the CPU to sleep
        asm::wfi(); 
    }
}
</code></pre>

<h2>4. Embedded Firmware Example</h2>
<p>During development, you might want to use a panic handler that talks to your debugger so you can see exactly <em>why</em> it crashed. A popular crate for this is `panic-halt` or `panic-probe`.</p>
<pre><code class="language-rust">// In Cargo.toml: panic-halt = "0.2.0"

#![no_std]
#![no_main]

// Just importing this crate defines the panic handler for you!
use panic_halt as _; 

#[cortex_m_rt::entry]
fn main() -> ! {
    let arr = [1, 2, 3];
    let crash = arr[5]; // This will immediately trigger the panic handler!
    loop {}
}
</code></pre>

<h2>5. Recap</h2>
<p>A panic is an unrecoverable error. In `#![no_std]`, you must define a `#[panic_handler]` to tell the microcontroller exactly how to safely shut down or halt when a panic occurs, preventing undefined behavior or hardware damage.</p>

<h2>6. Common Mistakes Beginners Make</h2>
<ul>
    <li>Forgetting to define a panic handler entirely. The compiler will throw an error saying `#[panic_handler]` is missing.</li>
    <li>Returning from a panic handler. Notice the `-> !` return type? That means this function <em>never</em> returns. It must contain an infinite loop.</li>
</ul>
"""
cha3 = """
<ol>
    <li><strong>Challenge 1:</strong> Why does a bare-metal panic handler have a return type of `-> !` (the Never type)?</li>
    <li><strong>Challenge 2:</strong> What could physically happen to a robot if a software panic occurs and the processor continues executing random memory instead of halting?</li>
</ol>
"""
ass3 = """
<p><strong>Assignment Idea:</strong> Write a custom `#[panic_handler]` that uses `cortex_m::asm::bkpt()` instead of `wfi()`. Research what `bkpt()` does and explain why it is highly useful during the debugging phase.</p>
"""
mcq3 = """
<ol>
    <li><strong>MCQ 1:</strong> What happens by default if an STM32 program panics without a defined panic handler? <br><em>(A) It restarts (B) It prints to the screen (C) It will not compile</em><br><strong>Answer: C</strong></li>
    <li><strong>MCQ 2:</strong> Which macro is used to define the emergency stop function in `#![no_std]` Rust? <br><em>(A) #[panic_handler] (B) #[error_handler] (C) #[interrupt]</em><br><strong>Answer: A</strong></li>
    <li><strong>MCQ 3:</strong> What does the return type `-> !` mean? <br><em>(A) Returns a boolean (B) Returns an error (C) The function never returns</em><br><strong>Answer: C</strong></li>
    <li><strong>MCQ 4:</strong> True or False: `panic-halt` is a crate that provides a simple infinite-loop panic handler. <br><strong>Answer: True</strong></li>
    <li><strong>MCQ 5:</strong> Why is `wfi()` (Wait For Interrupt) often used inside a panic loop? <br><em>(A) To save power while halted (B) To trigger a debugger (C) To restart the board</em><br><strong>Answer: A</strong></li>
</ol>
"""
process_and_save(l3, exp3, cha3, ass3, mcq3)

print("Module 3 fully seeded with Beginner-Friendly content and comics!")
