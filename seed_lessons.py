import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Course, Module, Lesson

course = Course.objects.filter(title="Rust on STM32").first()

if not course:
    print("Course not found!")
    exit()

# Create Module 1
module1, _ = Module.objects.update_or_create(
    course=course,
    title="Introduction to Rust for Embedded Systems (no_std)",
    defaults={"order": 1}
)

# --- LESSON 1 ---
lesson1_explanation = """
<h3>Why Rust for Embedded Systems?</h3>
<p>Embedded systems, especially those running on ARM Cortex-M microcontrollers like the STM32, have historically been programmed in C or C++. While these languages provide fine-grained control over hardware, they are notorious for memory safety bugs (buffer overflows, dangling pointers, use-after-free).</p>
<p>Rust solves this via its <strong>Ownership</strong> and <strong>Borrowing</strong> model, guaranteeing memory safety at compile-time without a garbage collector. This results in zero-cost abstractions—you get high-level ergonomics (iterators, closures) without runtime overhead.</p>

<h3>The <code>no_std</code> Environment</h3>
<p>Standard Rust programs rely on the standard library (<code>std</code>), which assumes the presence of an Operating System (for heap allocation, threads, networking, filesystem, etc.). Bare-metal microcontrollers do not have an OS.</p>
<p>Therefore, we use the <code>#![no_std]</code> attribute. This tells the Rust compiler to only link the <code>core</code> library, which contains fundamental types, traits, and functions that do not require an OS or an allocator.</p>

<pre style="background: #111; padding: 1rem; border-radius: 8px; color: #00f0ff; overflow-x: auto;">
<code>#![no_std]
#![no_main]

use core::panic::PanicInfo;

// We must define our own panic handler in a no_std environment
#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}
</code>
</pre>
<p>In the code above, the <code>!</code> return type indicates the function never returns (a diverging function). In an embedded system, if we panic, we usually just halt the CPU in an infinite loop.</p>
"""

lesson1_challenges = """
<ol>
    <li><strong>Compile Error Hunt:</strong> Write a standard Rust program using <code>Vec::new()</code> and compile it with <code>#![no_std]</code>. Analyze the compiler error.</li>
    <li><strong>Panic Handler Modification:</strong> Modify the provided panic handler to blink an LED (pseudocode) before entering the infinite loop.</li>
    <li><strong>Core vs Std:</strong> List 5 items that exist in <code>core</code> but not in <code>std</code>, and 5 that exist in <code>std</code> but not <code>core</code>.</li>
    <li><strong>Diverging Functions:</strong> Write 3 different functions that return the never type <code>!</code>.</li>
    <li><strong>No Main Attribute:</strong> Why do we need <code>#![no_main]</code> in bare-metal Rust? Explain what the standard main function expects.</li>
    <li><strong>Linker Script Setup:</strong> Research what a <code>memory.x</code> file is in the context of cortex-m-rt.</li>
    <li><strong>Size Constraints:</strong> Compare the binary size of a basic <code>std</code> hello world vs a <code>no_std</code> empty loop.</li>
    <li><strong>Heapless Crates:</strong> Look up the <code>heapless</code> crate. How does it provide <code>Vec</code> and <code>String</code> without a global allocator?</li>
    <li><strong>Safe Abstractions:</strong> Explain how Rust's safety guarantees apply even when we are forcing <code>no_std</code>.</li>
    <li><strong>Target Triples:</strong> What is the target triple for an STM32F4 microcontroller? How do you add it via rustup?</li>
</ol>
"""

lesson1_assignments = """
<ol>
    <li><strong>Setup the Environment:</strong> Install `rustup`, add the `thumbv7em-none-eabihf` target, and successfully compile a `#![no_std]` template project for ARM Cortex-M. Submit the `cargo build --release` output log.</li>
    <li><strong>Custom Panic Implementation:</strong> Write a custom panic handler that uses the `cortex_m::asm::bkpt()` macro to trigger a breakpoint when a debugger is attached.</li>
    <li><strong>Size Analysis:</strong> Use `cargo size` (from cargo-binutils) to analyze the memory footprint of your compiled `.elf` file. Document the sizes of the `.text`, `.data`, and `.bss` sections.</li>
</ol>
"""

lesson1_mcqs = """
<ol>
    <li style="margin-bottom: 1rem;"><strong>1. What does the `#![no_std]` attribute do?</strong><br>
        A) Disables all standard language features.<br>
        B) Links only the `core` library, omitting OS-dependent features.<br>
        C) Removes the need for a panic handler.<br>
        D) Optimizes the code for speed automatically.<br>
        <em>Answer: B</em>
    </li>
    <li style="margin-bottom: 1rem;"><strong>2. Which of the following is NOT available in `core`?</strong><br>
        A) `Option` and `Result`<br>
        B) Iterators<br>
        C) `std::fs::File`<br>
        D) Primitive types like `u32`<br>
        <em>Answer: C</em>
    </li>
    <li style="margin-bottom: 1rem;"><strong>3. What does the `!` return type signify in Rust?</strong><br>
        A) A function that returns a boolean.<br>
        B) A function that returns a Result with an Error.<br>
        C) A diverging function that never returns.<br>
        D) A macro invocation.<br>
        <em>Answer: C</em>
    </li>
    <!-- ... generating 7 more for the sake of completeness ... -->
    <li style="margin-bottom: 1rem;"><strong>4. Why is a custom panic handler required in `no_std`?</strong><br>
        A) The standard library provides the default panic handler, which is removed.<br>
        B) Embedded systems do not know what a panic is.<br>
        C) The compiler enforces it for speed.<br>
        D) To prevent hackers from exploiting memory.<br>
        <em>Answer: A</em>
    </li>
    <li style="margin-bottom: 1rem;"><strong>5. What is the purpose of `#![no_main]`?</strong><br>
        A) To tell the compiler the entry point is defined by the hardware/bootloader.<br>
        B) To make the program run faster.<br>
        C) To allow multiple main functions.<br>
        D) To compile a library instead of a binary.<br>
        <em>Answer: A</em>
    </li>
    <li style="margin-bottom: 1rem;"><strong>6. Which architecture is STM32 based on?</strong><br>
        A) x86_64<br>
        B) ARM Cortex-M<br>
        C) RISC-V<br>
        D) AVR<br>
        <em>Answer: B</em>
    </li>
    <li style="margin-bottom: 1rem;"><strong>7. What happens if you try to allocate a `String` in a strict `no_std` environment (without an allocator)?</strong><br>
        A) The program panics at runtime.<br>
        B) The compiler throws an error because `String` is not in `core`.<br>
        C) The memory is allocated on the stack.<br>
        D) The garbage collector handles it.<br>
        <em>Answer: B</em>
    </li>
    <li style="margin-bottom: 1rem;"><strong>8. How does Rust achieve memory safety?</strong><br>
        A) Garbage Collection<br>
        B) Reference Counting exclusively<br>
        C) Compile-time Ownership and Borrow Checking<br>
        D) Manual `free()` calls<br>
        <em>Answer: C</em>
    </li>
    <li style="margin-bottom: 1rem;"><strong>9. Which tool is commonly used to flash Rust code to an STM32?</strong><br>
        A) cargo-flash / probe-rs<br>
        B) gcc<br>
        C) make<br>
        D) avrdude<br>
        <em>Answer: A</em>
    </li>
    <li style="margin-bottom: 1rem;"><strong>10. Zero-cost abstractions mean:</strong><br>
        A) The code costs nothing to write.<br>
        B) High-level code compiles to the same machine code as hand-written low-level code.<br>
        C) Abstractions use zero memory on the stack.<br>
        D) There are zero abstractions allowed in the code.<br>
        <em>Answer: B</em>
    </li>
</ol>
"""

Lesson.objects.update_or_create(
    module=module1,
    title="1. What is no_std and why Rust?",
    defaults={
        "order": 1,
        "explanation_html": lesson1_explanation,
        "challenges_html": lesson1_challenges,
        "assignments_html": lesson1_assignments,
        "mcqs_html": lesson1_mcqs
    }
)

# --- LESSON 2 ---
lesson2_explanation = """
<h3>Creating your first Cargo Embedded Project</h3>
<p>To begin, we need to setup Cargo for an embedded target. We will use the <code>cargo-generate</code> tool to pull a Cortex-M quickstart template.</p>
<pre style="background: #111; padding: 1rem; border-radius: 8px; color: #00f0ff; overflow-x: auto;">
<code>cargo install cargo-generate
cargo generate --git https://github.com/rust-embedded/cortex-m-quickstart
</code>
</pre>

<p>This generates a project pre-configured with a <code>.cargo/config.toml</code> and a <code>memory.x</code> file.</p>
<h4>The <code>.cargo/config.toml</code></h4>
<p>This file tells Cargo exactly how to compile and run your code. For STM32, we typically set the target and the runner (like `probe-run` or `openocd`).</p>
<pre style="background: #111; padding: 1rem; border-radius: 8px; color: #00f0ff; overflow-x: auto;">
<code>[build]
target = "thumbv7em-none-eabihf"

[target.thumbv7em-none-eabihf]
runner = "probe-rs run --chip STM32F411RETx"
rustflags = [
  "-C", "link-arg=-Tlink.x",
]
</code>
</pre>
<p>Now, running <code>cargo run</code> will compile your code, connect to the microcontroller via SWD, flash the binary, and open a defmt/rtt console!</p>
"""

Lesson.objects.update_or_create(
    module=module1,
    title="2. Getting Started with Cargo & Flashing",
    defaults={
        "order": 2,
        "explanation_html": lesson2_explanation,
        "challenges_html": "<p>10 challenges coming soon...</p>",
        "assignments_html": "<p>3 assignments coming soon...</p>",
        "mcqs_html": "<p>10 MCQs coming soon...</p>"
    }
)

print("Successfully seeded Module 1 and lessons!")
