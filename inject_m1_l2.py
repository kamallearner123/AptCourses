import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Course, Module, Lesson

course = Course.objects.get(title="Rust on STM32")
module = Module.objects.get(course=course, order=1)
lesson = Lesson.objects.get(module=module, order=2)

with open('m1_l2_content.html', 'r') as f:
    content = f.read()

lesson.explanation_html = content

lesson.challenges_html = """
<ol>
    <li><strong>Scenario Challenge 1:</strong> You are designing a battery-powered IoT tracker that pings GPS data once an hour. Which STM32 family should you choose and why?</li>
    <li><strong>Scenario Challenge 2:</strong> Your firmware team is migrating from STM32F1 to STM32F4. Explain the key architectural differences in the Cortex-M cores they need to be aware of.</li>
    <li><strong>Scenario Challenge 3:</strong> You attempt to compile a Rust binary for an STM32G0 using `thumbv7em-none-eabihf`. Explain why the compiler/linker will fail or produce invalid firmware.</li>
    <li><strong>Scenario Challenge 4:</strong> You need to perform heavy DSP (Digital Signal Processing) on audio data. Which ARM Cortex-M feature do you need, and which STM32 family provides it?</li>
    <li><strong>Scenario Challenge 5:</strong> Defend the decision to use the STM32F401RE for a beginner Rust course over a newer, more powerful H7 chip.</li>
    <li><strong>Interview Challenge 1:</strong> "What does the 'E' in STM32F401RET6 indicate about its memory capacity?"</li>
    <li><strong>Interview Challenge 2:</strong> "Explain the difference between a PAC (Peripheral Access Crate) and a HAL in the Rust embedded ecosystem."</li>
    <li><strong>Interview Challenge 3:</strong> "If ST doesn't design the Cortex-M CPU, what exactly do they design in an STM32 microcontroller?"</li>
    <li><strong>Interview Challenge 4:</strong> "What is `svd2rust`, and why is it critical for the `stm32-rs` ecosystem?"</li>
    <li><strong>Interview Challenge 5:</strong> "Why might you choose a chip with an M0+ core over an M4 core?"</li>
</ol>
"""

lesson.assignments_html = """
<ol>
    <li><strong>Chip Decoding:</strong> Decode the part number <strong>STM32L476VGT6</strong>. List its Family, Core, Pin Count, and Flash Size using the naming convention guide.</li>
    <li><strong>Toolchain Setup:</strong> Based on the core you identified in Assignment 1, determine the exact `rustup target add` command required to cross-compile for that chip.</li>
    <li><strong>Ecosystem Audit:</strong> Go to the `stm32-rs` GitHub organization. Find the HAL repository for the STM32F4 family and check the README to see if the I2C peripheral is fully supported.</li>
</ol>
"""

lesson.mcqs_html = """
<ol>
    <li><strong>MCQ 1:</strong> Which company designs the Cortex-M CPU core architecture? <br><em>(A) STMicroelectronics (B) ARM Holdings (C) Intel</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 2:</strong> Which STM32 family is explicitly designed for Ultra-Low Power applications? <br><em>(A) F-Series (B) H-Series (C) L-Series</em><br><strong>Answer: C</strong></li>
    <li><strong>MCQ 3:</strong> What target triple should you use for an STM32F4 with a hardware Floating Point Unit (FPU)? <br><em>(A) thumbv6m-none-eabi (B) thumbv7em-none-eabi (C) thumbv7em-none-eabihf</em><br><strong>Answer: C</strong></li>
    <li><strong>MCQ 4:</strong> The letter 'R' in STM32F401RET6 signifies how many pins? <br><em>(A) 48 (B) 64 (C) 100</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 5:</strong> Which tool automatically generates PACs from manufacturer XML files? <br><em>(A) cargo-flash (B) svd2rust (C) cortex-m-rt</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 6:</strong> What does DSP stand for in the context of the Cortex-M4? <br><em>(A) Digital Signal Processing (B) Direct Stack Pointer (C) Dynamic System Power</em><br><strong>Answer: A</strong></li>
    <li><strong>MCQ 7:</strong> True or False: The STM32H7 is an entry-level, low-power microcontroller. <br><strong>Answer: False</strong></li>
    <li><strong>MCQ 8:</strong> True or False: A PAC provides high-level functions like `led.set_high()`. <br><strong>Answer: False</strong> (That's a HAL. PACs provide raw register access).</li>
    <li><strong>MCQ 9:</strong> What memory size does the 'E' in STM32F401RE indicate? <br><em>(A) 128KB (B) 256KB (C) 512KB</em><br><strong>Answer: C</strong></li>
    <li><strong>MCQ 10:</strong> Which board is highly recommended for beginners learning Embedded Rust? <br><em>(A) STM32H753I-EVAL (B) NUCLEO-F401RE (C) Arduino Uno</em><br><strong>Answer: B</strong></li>
</ol>
"""

lesson.save()
print(f"Successfully injected corporate training textbook content into {lesson.title}!")
