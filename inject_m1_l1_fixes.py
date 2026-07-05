import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Course, Module, Lesson

course = Course.objects.get(title="Rust on STM32")
module = Module.objects.get(course=course, order=1)
lesson = Lesson.objects.get(module=module, order=1)

# Ensure the explanation doesn't have the hardcoded knowledge check at the end
# (We will just keep it there, it doesn't hurt, but we will populate the REAL fields)

lesson.challenges_html = """
<ol>
    <li><strong>Scenario Challenge 1:</strong> You are tasked with migrating a legacy C codebase for an automotive braking system. Explain how you would justify the transition to Rust to a skeptical project manager.</li>
    <li><strong>Scenario Challenge 2:</strong> A junior engineer writes a C function that modifies a global buffer from an interrupt. Explain the race condition and how Rust's ownership prevents this.</li>
    <li><strong>Scenario Challenge 3:</strong> You need to ensure a DMA transfer buffer is not freed before the transfer completes. Explain how Rust lifetimes solve this natively compared to C.</li>
    <li><strong>Scenario Challenge 4:</strong> Why is `cortex-m-rt` used instead of writing your own assembly startup script?</li>
    <li><strong>Scenario Challenge 5:</strong> Defend the use of Zero-Cost abstractions (like iterators) in a bare-metal environment with strict 32KB RAM limits.</li>
    <li><strong>Interview Challenge 1:</strong> "Explain the difference between the Stack and the Heap. Why do we avoid the Heap in embedded Rust?"</li>
    <li><strong>Interview Challenge 2:</strong> "How does Rust guarantee memory safety without a garbage collector?"</li>
    <li><strong>Interview Challenge 3:</strong> "What is a Dangling Pointer, and how does the Borrow Checker prevent it?"</li>
    <li><strong>Interview Challenge 4:</strong> "What is the difference between a PAC and a HAL?"</li>
    <li><strong>Interview Challenge 5:</strong> "Explain Monomorphization in the context of generic functions."</li>
</ol>
"""

lesson.assignments_html = """
<ol>
    <li><strong>Environment Audit:</strong> Run `rustup show` and `cargo -V` on your machine. Submit the terminal output to prove your toolchain is correctly installed.</li>
    <li><strong>Memory Map Diagram:</strong> Using the Reference Manual for your specific STM32 board, draw a Mermaid diagram (or write a summary) of the memory layout (Flash, SRAM, Peripherals).</li>
    <li><strong>Code Comparison Report:</strong> Write a 1-page markdown report comparing a C buffer overflow vulnerability to its Rust counterpart. Compile both snippets mentally or via Godbolt and submit your analysis.</li>
</ol>
"""

lesson.mcqs_html = """
<ol>
    <li><strong>MCQ 1:</strong> Which organization originally sponsored the creation of Rust? <br><em>(A) Google (B) Mozilla (C) Microsoft</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 2:</strong> What is a Double Free error? <br><em>(A) Freeing memory twice, causing corruption (B) A promotional discount (C) Reallocating an array</em><br><strong>Answer: A</strong></li>
    <li><strong>MCQ 3:</strong> Does Rust use a Garbage Collector? <br><em>(A) Yes (B) No</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 4:</strong> What does MISRA C rely on to enforce safety? <br><em>(A) The Compiler (B) Static Analyzers (C) Garbage Collection</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 5:</strong> What is the base address of Flash memory in an STM32? <br><em>(A) 0x2000_0000 (B) 0x0800_0000 (C) 0x4000_0000</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 6:</strong> Which crate provides core ARM architecture functions like the NVIC? <br><em>(A) stm32f4xx-hal (B) cortex-m (C) svd2rust</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 7:</strong> True or False: Rust allows multiple mutable references to the same data simultaneously. <br><strong>Answer: False</strong></li>
    <li><strong>MCQ 8:</strong> True or False: Zero-cost abstractions mean the compiled code has no runtime overhead compared to equivalent C code. <br><strong>Answer: True</strong></li>
    <li><strong>MCQ 9:</strong> What compiler backend does Rust use? <br><em>(A) GCC (B) LLVM (C) MSVC</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 10:</strong> Which tool is commonly used to flash Rust binaries to an STM32? <br><em>(A) probe-rs (B) cargo-flash (C) Both A & B</em><br><strong>Answer: C</strong></li>
</ol>
"""

lesson.save()
print("Fixed Lesson M1.1 Assignments, Challenges, and MCQs!")
