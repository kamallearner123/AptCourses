import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Course, Module, Lesson
from hide_mcq_answers_v2 import transform_mcqs_global

course = Course.objects.get(title="Rust on STM32")
module = Module.objects.get(course=course, order=1)
l3 = Lesson.objects.get(module=module, order=3)

# 1. Main Explanation HTML
explanation = """
<img src="/static/images/comic_m1_l3.png" alt="Hardware Safety and ESD Comic" style="width: 100%; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid rgba(0,240,255,0.3);">

<h2>1. The Invisible Threat: Electrostatic Discharge (ESD)</h2>
<p>As a software engineer transitioning into embedded systems, your first physical hurdle is not the compiler—it's your own body. Human beings naturally build up static electricity just by walking across a carpet or shifting in a chair.</p>
<p><strong>Why it destroys chips:</strong><br>
Modern microcontrollers, like the Cortex-M cores found in STM32 families, are fabricated using advanced CMOS (Complementary Metal-Oxide-Semiconductor) technology. The oxide layers inside these transistors are incredibly thin (often measured in nanometers). A static shock that you can barely feel (around 3,000 volts) can easily puncture these oxide layers, instantly killing the MCU or, worse, causing intermittent "walking wounded" failures that take hours to debug.</p>

<hr>

<h2>2. Hardware Handling Best Practices</h2>
<p>To ensure your development board survives this course, strictly follow these handling procedures:</p>
<ul>
    <li><strong>Anti-Static Wrist Straps:</strong> Always wear a grounded ESD wrist strap when handling bare PCBA (Printed Circuit Board Assemblies).</li>
    <li><strong>Hold by the Edges:</strong> Never touch the exposed pins of the STM32 chip or the header pins. Oils and static from your fingers are detrimental.</li>
    <li><strong>Safe Storage:</strong> When not in use, store your board in a static-shielding bag (the shiny silver ones, not the pink anti-static ones, which only prevent charge generation but do not shield).</li>
</ul>

<hr>

<h2>3. Electrical Limits and Magic Smoke</h2>
<p>Unlike software where a bug throws a segmentation fault, hardware bugs result in physical destruction (often referred to colloquially as letting the "Magic Smoke" out).</p>
<ul>
    <li><strong>Voltage Constraints:</strong> STM32 microcontrollers generally operate at <strong>3.3V</strong>. Applying 5V directly to a non-5V-tolerant GPIO pin will destroy the internal clamping diodes and ruin the pin (or the whole chip).</li>
    <li><strong>Current Limits:</strong> A single STM32 GPIO pin can typically source or sink an absolute maximum of <strong>25mA</strong>. If you try to drive a high-power motor directly from a GPIO pin without a transistor or motor driver, the MCU will burn out.</li>
</ul>

<hr>

<h2>4. Software-Hardware Safety: Panic Handlers</h2>
<p>Hardware safety isn't just about static electricity; it's also about what the hardware does when the software fails. In Rust, if an unrecoverable error occurs, the system <em>panics</em>. On an STM32, we must explicitly define what happens during a panic to prevent hardware damage (e.g., stopping PWM signals to a motor).</p>

<pre><code class="language-rust">// A safe, minimal panic handler for STM32
#![no_std]
#![no_main]

use core::panic::PanicInfo;
use cortex_m_rt::entry;

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    // In a real system, you would disable motors/actuators here
    // before halting the processor.
    loop {
        // Halt the CPU completely to prevent unpredictable behavior
        cortex_m::asm::wfi(); 
    }
}

#[entry]
fn main() -> ! {
    // Firmware logic
    loop {}
}
</code></pre>
"""

# 2. Challenges
challenges = """
<ol>
    <li><strong>Scenario Challenge 1:</strong> You are debugging an STM32 board that occasionally resets itself when you touch the desk. Explain the likely physical cause based on the principles of ESD.</li>
    <li><strong>Scenario Challenge 2:</strong> Explain why a static shock you cannot even feel is still highly dangerous to a Cortex-M MCU based on its CMOS fabrication.</li>
    <li><strong>Scenario Challenge 3:</strong> You need to control a DC motor that draws 1A. Why can't you connect it directly to an STM32 GPIO pin?</li>
    <li><strong>Scenario Challenge 4:</strong> What is the difference between a static-shielding bag and a pink anti-static bag?</li>
    <li><strong>Scenario Challenge 5:</strong> In your Rust `#[panic_handler]`, why is it critical to safely shut down hardware (like a heating element) before halting the CPU?</li>
    <li><strong>Interview Challenge 1:</strong> "What is the typical operating voltage for most STM32 microcontrollers?"</li>
    <li><strong>Interview Challenge 2:</strong> "What does it mean when a GPIO pin is described as '5V-tolerant'?"</li>
    <li><strong>Interview Challenge 3:</strong> "Explain the mechanism of failure when an oxide layer in a CMOS transistor is punctured."</li>
    <li><strong>Interview Challenge 4:</strong> "What does the `wfi` instruction do in an ARM Cortex-M, and why use it in a panic handler?"</li>
    <li><strong>Interview Challenge 5:</strong> "What is a 'walking wounded' component?"</li>
</ol>
"""

# 3. Assignments
assignments = """
<ol>
    <li><strong>Datasheet Audit:</strong> Download the datasheet for the STM32F401RE. Find the "Absolute Maximum Ratings" table and submit the maximum allowed voltage on a standard VDD pin.</li>
    <li><strong>Current Limit Check:</strong> In the same datasheet, find the absolute maximum total current (I_VDD) the entire chip is allowed to draw.</li>
    <li><strong>Safety Code:</strong> Write a custom Rust `#[panic_handler]` that uses `cortex_m::asm::bkpt()` instead of `wfi()` to trigger a debugger breakpoint on failure.</li>
</ol>
"""

# 4. MCQs
mcqs = """
<ol>
    <li><strong>MCQ 1:</strong> What is the typical operating voltage for an STM32 microcontroller? <br><em>(A) 5.0V (B) 3.3V (C) 1.8V</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 2:</strong> How thin are the oxide layers in modern CMOS transistors? <br><em>(A) Millimeters (B) Micrometers (C) Nanometers</em><br><strong>Answer: C</strong></li>
    <li><strong>MCQ 3:</strong> What is the absolute maximum current a single standard STM32 GPIO pin should safely source/sink? <br><em>(A) 5mA (B) 25mA (C) 500mA</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 4:</strong> Which bag actually protects components from external electrostatic fields? <br><em>(A) Pink anti-static bag (B) Silver static-shielding bag (C) Standard plastic ziplock</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 5:</strong> What does "walking wounded" mean in electronics? <br><em>(A) A chip that gets hot (B) A chip that suffered ESD damage and fails intermittently (C) A battery running out of charge</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 6:</strong> What macro is used to define the panic behavior in a `#![no_std]` Rust binary? <br><em>(A) #[panic_handler] (B) #[entry] (C) #[fatal_error]</em><br><strong>Answer: A</strong></li>
    <li><strong>MCQ 7:</strong> True or False: You should always handle a bare PCB by its edges. <br><strong>Answer: True</strong></li>
    <li><strong>MCQ 8:</strong> True or False: Humans can feel a static shock of 500 volts. <br><strong>Answer: False</strong> (Usually takes ~3000V to feel it).</li>
    <li><strong>MCQ 9:</strong> What instruction halts the Cortex-M CPU until an interrupt occurs, saving power? <br><em>(A) halt (B) bkpt (C) wfi</em><br><strong>Answer: C</strong></li>
    <li><strong>MCQ 10:</strong> Why do we avoid connecting a 5V signal to a 3.3V non-tolerant pin? <br><em>(A) It will run too slowly (B) It destroys internal clamping diodes (C) It will drain the battery</em><br><strong>Answer: B</strong></li>
</ol>
"""

# Apply the rules
l3.explanation_html = explanation
l3.challenges_html = challenges
l3.assignments_html = assignments
l3.mcqs_html = transform_mcqs_global(mcqs)

# Apply Rule 2 (Abbreviations) to all fields natively
from highlight_abbreviations import highlight_text
l3.explanation_html = highlight_text(l3.explanation_html)
l3.challenges_html = highlight_text(l3.challenges_html)
l3.assignments_html = highlight_text(l3.assignments_html)
l3.mcqs_html = highlight_text(l3.mcqs_html)

l3.save()
print("Successfully seeded M1.3 Hardware Safety Basics!")
