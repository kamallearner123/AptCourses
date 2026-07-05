import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Course, Module, Lesson
from hide_mcq_answers_v2 import transform_mcqs_global
from highlight_abbreviations import highlight_text

course = Course.objects.get(title="Rust on STM32")
module = Module.objects.get(course=course, order=2)

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

<h2>1. A Simple Explanation: What are Variables?</h2>
<p>Welcome! Think of a variable in Rust as a labeled box where you can store a piece of data. When you want to use that data later, you just ask for the box by its label. In Rust, you create these boxes using the <code>let</code> keyword (called a binding).</p>
<p>By default, Rust variables are <strong>immutable</strong>. This means once you put something in the box, the box is sealed tight! You can't change the contents. If you want a box that can be opened and updated, you must explicitly declare it as <strong>mutable</strong> using <code>let mut</code>.</p>
<p>Rust also allows <strong>variable shadowing</strong>, meaning you can declare a new variable with the exact same name as an old one, effectively replacing it. For naming conventions, Rust prefers <code>snake_case</code> (e.g., <code>sensor_reading</code>).</p>

<h2>2. Why It Matters</h2>
<p>Immutability by default is a superpower for safety. It prevents accidental changes to data that shouldn't change, which is a massive source of bugs in other languages. In embedded systems, knowing exactly how much memory a variable uses is critical because microcontrollers have very little RAM. Rust's strict <strong>scalar data types</strong> (single values) and <strong>compound data types</strong> (multiple values) give you exact control.</p>

<h2>3. Small Code Example</h2>
<pre><code class="language-rust">let pin_number = 5; // Immutable, type inferred as i32 usually, but here likely u8
let mut click_count = 0; // Mutable
click_count += 1;

// Shadowing example:
let temperature = "25"; // A string
let temperature: u8 = 25; // Shadowed into a number!
</code></pre>

<h2>4. The Data Types in Embedded Rust</h2>
<p>Rust has strict types. While it has <strong>Type Inference</strong> (it can guess the type), you will often use <strong>Type Annotations</strong> in embedded code.</p>
<ul>
    <li><strong>Integers:</strong> Signed (can be negative: <code>i8, i16, i32</code>) and Unsigned (positive only: <code>u8, u16, u32</code>). On an STM32, <code>u8</code> is perfect for a pin state, while <code>u32</code> is great for a system timer.</li>
    <li><strong>Floating-point:</strong> <code>f32</code> and <code>f64</code> for decimal numbers.</li>
    <li><strong>Boolean:</strong> <code>bool</code> (true or false). Perfect for LED states.</li>
    <li><strong>Character:</strong> <code>char</code> (a single unicode character).</li>
    <li><strong>Tuples:</strong> Grouping different types together. Example: returning both a temperature and a humidity value.</li>
    <li><strong>Arrays:</strong> Grouping the same types together with a fixed length. Example: A buffer of 64 bytes for receiving UART data.</li>
</ul>

<h2>5. Embedded Firmware Example</h2>
<pre><code class="language-rust">// Storing an LED state
let is_led_on: bool = true;

// Using an array for a data buffer
let mut uart_buffer: [u8; 64] = [0; 64];

// Using a tuple to group sensor readings
let sensor_reading: (u16, f32) = (1024, 23.5); // (Raw ADC value, Celsius)
</code></pre>

<h2>6. Recap</h2>
<p>Variables are immutable by default (`let`) but can be made mutable (`let mut`). Rust provides precise integer sizes (`u8`, `u32`) which are vital for memory-constrained embedded systems. Arrays hold identical types, while Tuples hold mixed types.</p>

<h2>7. Common Mistakes Beginners Make</h2>
<ul>
    <li>Forgetting `mut` when trying to update a variable. The compiler will kindly remind you!</li>
    <li>Trying to put a negative number into an unsigned type (e.g., `let x: u8 = -5;`).</li>
    <li>Letting the compiler infer an `i32` when you actually needed a `u8` to talk to an 8-bit hardware register.</li>
</ul>
"""
cha1 = """
<ol>
    <li><strong>Challenge 1:</strong> Declare an immutable variable holding the pin number 13 as a `u8`.</li>
    <li><strong>Challenge 2:</strong> Declare a mutable variable to count button presses, initialized to 0.</li>
    <li><strong>Challenge 3:</strong> Write an array declaration for an SPI transmit buffer that holds four `u8` values: 10, 20, 30, and 40.</li>
</ol>
"""
ass1 = """
<p><strong>Assignment Idea:</strong> Create a small Rust script that uses a tuple to represent an (X, Y, Z) accelerometer reading using `i16` integers. Write a function that takes this tuple and returns the X value.</p>
"""
mcq1 = """
<ol>
    <li><strong>MCQ 1:</strong> Which keyword makes a variable modifiable in Rust? <br><em>(A) let (B) mut (C) var</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 2:</strong> Which type is best for an array acting as a serial data buffer? <br><em>(A) f32 (B) char (C) u8</em><br><strong>Answer: C</strong></li>
    <li><strong>MCQ 3:</strong> What is variable shadowing? <br><em>(A) Hiding a variable in memory (B) Re-declaring a new variable with the same name (C) Creating a pointer</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 4:</strong> What type can hold multiple different data types grouped together? <br><em>(A) Array (B) Tuple (C) Slice</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 5:</strong> Why are unsigned integers (`u8`, `u32`) heavily used in embedded systems? <br><em>(A) They support fractions (B) Hardware registers don't have negative memory addresses or values (C) They are faster</em><br><strong>Answer: B</strong></li>
</ol>
"""
process_and_save(l1, exp1, cha1, ass1, mcq1)

# ==========================================
# M2.2: Ownership & Borrowing
# ==========================================
l2 = Lesson.objects.get(module=module, order=2)
exp2 = """
<img src="/static/images/comic_m2_l2.png" alt="Ownership Comic" style="width: 100%; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid rgba(255,0,127,0.3);">

<h2>1. A Simple Explanation: Ownership and Borrowing</h2>
<p>Imagine a book. In Rust, every piece of data has an <strong>Owner</strong> (the person holding the book). When the owner walks out of the room (goes out of scope), they throw the book in the trash (memory is freed). There can only ever be ONE owner at a time.</p>
<p>If you want to give the book to a friend, you <strong>move</strong> ownership to them. Now you can't read it anymore! But what if you just want them to look at it without taking it permanently? You let them <strong>borrow</strong> it using <strong>References</strong>.</p>
<ul>
    <li><strong>Immutable Borrow (<code>&amp;</code>):</strong> Like a museum exhibit. Many people can look at the book at the same time, but nobody can write in it.</li>
    <li><strong>Mutable Borrow (<code>&amp;mut</code>):</strong> Like giving someone a pen. Exactly ONE person can write in the book, and nobody else is allowed to even look at it until they are done.</li>
</ul>

<h2>2. Why It Matters</h2>
<p>These three Ownership Rules are Rust's magic spell. They completely eliminate entire classes of bugs like dangling pointers, double-frees, and data races. In embedded firmware, this means two hardware interrupts can never accidentally overwrite the same memory buffer at the exact same time.</p>
<p><em>Stack vs Heap:</em> In beginner embedded Rust, we almost exclusively use the <strong>Stack</strong> (fast, fixed-size memory). We avoid the <strong>Heap</strong> (dynamic, variable-size memory) because it can lead to fragmentation. Types like `u8` are <strong>Copy types</strong> (they are so small they are copied on the stack instead of moved). Complex types move.</p>

<h2>3. Small Code Example</h2>
<pre><code class="language-rust">fn main() {
    let sensor_config = String::from("Config A");
    // print_config(sensor_config); // If we did this, ownership MOVES to the function.
    
    // Instead, we BORROW it:
    borrow_config(&sensor_config); 
    
    // We can still use it!
    println!("Still have: {}", sensor_config);
}

fn borrow_config(config: &String) {
    println!("Reading: {}", config); // Dereferencing happens automatically here
}
</code></pre>

<h2>4. Embedded Firmware Example</h2>
<p>In firmware, we often borrow a <strong>Slice</strong> (a view into part of an array) to safely process UART data without taking ownership of the whole buffer.</p>
<pre><code class="language-rust">fn process_command(buffer: &[u8]) {
    if buffer[0] == 0x01 {
        // Turn on LED
    }
}

let mut uart_rx = [0u8; 64];
// We received 4 bytes, so we borrow a slice of just those 4 bytes!
process_command(&uart_rx[0..4]); 
</code></pre>

<h2>5. Recap</h2>
<p>Every value has one owner. When the owner scope ends, memory is freed. You can borrow data immutably (`&`) many times, OR mutably (`&mut`) exactly once. Slices are borrowed views into arrays.</p>

<h2>6. Common Mistakes Beginners Make</h2>
<ul>
    <li>Trying to use a variable after passing it to a function (moving ownership) instead of passing a reference.</li>
    <li>Trying to create a mutable borrow (`&mut`) while an immutable borrow (`&`) still exists. The <strong>Borrow Checker</strong> will stop you!</li>
</ul>
"""
cha2 = """
<ol>
    <li><strong>Challenge 1:</strong> You have an array `let buffer = [1, 2, 3];`. Write the code to pass a slice of the first two elements to a function.</li>
    <li><strong>Challenge 2:</strong> Explain in your own words why Rust doesn't let you have two `&mut` references to the same variable at the same time.</li>
</ol>
"""
ass2 = """
<p><strong>Assignment Idea:</strong> Write a function `update_state(state: &mut u8)` that increments the passed variable by 1. Call it from `main` using a mutable reference.</p>
"""
mcq2 = """
<ol>
    <li><strong>MCQ 1:</strong> What happens to a value when its owner goes out of scope? <br><em>(A) It is saved to disk (B) It is dropped and freed (C) It waits for garbage collection</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 2:</strong> How many mutable borrows (`&mut`) are allowed for a piece of data at one time? <br><em>(A) Exactly one (B) Two (C) Unlimited</em><br><strong>Answer: A</strong></li>
    <li><strong>MCQ 3:</strong> What is a slice in Rust? <br><em>(A) A new copy of an array (B) A borrowed view into a contiguous sequence (C) A heap allocation</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 4:</strong> True or False: Simple types like `u32` are "Copy types", meaning they are copied rather than moved. <br><strong>Answer: True</strong></li>
    <li><strong>MCQ 5:</strong> What tool enforces these rules at compile time? <br><em>(A) The Garbage Collector (B) The Borrow Checker (C) The Linker</em><br><strong>Answer: B</strong></li>
</ol>
"""
process_and_save(l2, exp2, cha2, ass2, mcq2)


# ==========================================
# M2.3: Enums & Pattern Matching
# ==========================================
l3 = Lesson.objects.get(module=module, order=3)
exp3 = """
<img src="/static/images/comic_m2_l3.png" alt="Enums Comic" style="width: 100%; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid rgba(0,240,255,0.3);">

<h2>1. A Simple Explanation: Enums and Match</h2>
<p>An <strong>Enum</strong> (short for enumeration) allows you to define a type by listing its possible variants. Imagine a traffic light: it can only be Red, Yellow, or Green. It can't be "Apple." Enums let you define exactly what states exist. Better yet, in Rust, enum variants can hold data inside them!</p>
<p>To interact with Enums, we use <strong>Pattern Matching</strong> via the <code>match</code> keyword. It’s like a super-powered <code>switch</code> statement. The compiler forces <strong>Exhaustiveness</strong>: you MUST handle every single possible variant, or the code won't compile.</p>

<h2>2. Why It Matters</h2>
<p>In embedded systems, tracking the "State" of the device is everything. Is the device Idle? Measuring? Transmitting? In Error? Using Enums to model system states prevents invalid states. Furthermore, Rust provides two built-in Enums: <code>Option</code> (for things that might be missing) and <code>Result</code> (for things that might fail), which eliminate Null Pointer crashes entirely!</p>

<h2>3. Small Code Example</h2>
<pre><code class="language-rust">enum DeviceState {
    Idle,
    Measuring,
    Error(u8), // This variant holds a u8 error code payload!
}

let current_state = DeviceState::Error(404);

match current_state {
    DeviceState::Idle => println!("Waiting..."),
    DeviceState::Measuring => println!("Taking data..."),
    DeviceState::Error(code) => println!("Failed with code: {}", code),
    // If we forgot a variant, the compiler would fail!
}
</code></pre>

<h2>4. Embedded Firmware Example</h2>
<p>Sometimes you only care about ONE specific pattern and want to ignore the rest. You can use <code>if let</code> (or use the <code>_</code> wildcard in a match block).</p>
<pre><code class="language-rust">// Reading an I2C sensor that returns a Result
let sensor_result = read_temperature();

// Using if let to only execute if it was successful (Ok)
if let Ok(temp) = sensor_result {
    turn_on_heater(temp);
} else {
    // It was an Err, we ignore or handle it simply
}
</code></pre>

<h2>5. Recap</h2>
<p>Enums group distinct variants into a single type, and variants can hold data payloads. <code>match</code> is an exhaustive control flow tool that routes logic based on the pattern. <code>if let</code> is a shorthand for matching a single pattern.</p>

<h2>6. Common Mistakes Beginners Make</h2>
<ul>
    <li>Forgetting to handle a variant in a `match` block. (Fix: add the missing arm, or use `_ => {}` as a catch-all wildcard).</li>
    <li>Trying to extract the payload from an enum without using a `match` or `if let`.</li>
</ul>
"""
cha3 = """
<ol>
    <li><strong>Challenge 1:</strong> Define an Enum called `ButtonEvent` with variants `Pressed`, `Released`, and `Held(u32)` where the u32 is duration.</li>
    <li><strong>Challenge 2:</strong> Write a `match` block that catches all unhandled cases using the `_` wildcard.</li>
</ol>
"""
ass3 = """
<p><strong>Assignment Idea:</strong> Create a function that takes an `Option<u8>`. Use `match` to return the number if it exists (`Some`), or return 0 if it is `None`.</p>
"""
mcq3 = """
<ol>
    <li><strong>MCQ 1:</strong> Can Rust enums carry data payloads (like integers or structs) inside their variants? <br><em>(A) Yes (B) No</em><br><strong>Answer: A</strong></li>
    <li><strong>MCQ 2:</strong> What does "exhaustiveness" mean in a `match` block? <br><em>(A) It runs very slowly (B) Every possible enum variant must be handled (C) It consumes memory</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 3:</strong> What symbol is used as the catch-all wildcard pattern? <br><em>(A) * (B) default (C) _</em><br><strong>Answer: C</strong></li>
    <li><strong>MCQ 4:</strong> If you only care about matching ONE specific variant, what is the cleanest syntax? <br><em>(A) if let (B) while let (C) switch</em><br><strong>Answer: A</strong></li>
    <li><strong>MCQ 5:</strong> Which built-in Enum is used to handle operations that might succeed or fail? <br><em>(A) Option (B) Result (C) Status</em><br><strong>Answer: B</strong></li>
</ol>
"""
process_and_save(l3, exp3, cha3, ass3, mcq3)

# ==========================================
# M2.4: Traits & Lifetimes
# ==========================================
l4 = Lesson.objects.get(module=module, order=4)
exp4 = """
<img src="/static/images/comic_m2_l4.png" alt="Lifetimes Comic" style="width: 100%; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid rgba(255,0,127,0.3);">

<h2>1. A Simple Explanation: Traits and Lifetimes</h2>
<p><strong>Traits:</strong> Imagine a job description. A job description doesn't do any work, it just lists the skills required (e.g., "Must be able to Drive"). In Rust, a Trait is exactly that—a behavior contract. If a type implements a Trait, it promises it has those specific methods.</p>
<p><strong>Lifetimes:</strong> Remember Borrowing? If you loan someone your book, they have to give it back before the book is destroyed. A Lifetime (written with a tick mark, like <code>'a</code>) is a label the compiler uses to track relationships between references over time, ensuring a reference NEVER points to deleted data.</p>

<h2>2. Why It Matters</h2>
<p>Traits are the backbone of reusable embedded code. The <code>embedded-hal</code> crate is just a giant list of Traits (like <code>OutputPin</code>). Because of this, you can write a driver for an LCD screen that works on ANY microcontroller, as long as the microcontroller implements the <code>OutputPin</code> trait!</p>
<p>Lifetimes are how Rust achieves memory safety without a garbage collector. The compiler usually infers them automatically, but when you store a reference <em>inside a struct</em>, you must use explicit lifetime annotations so the compiler knows how long that struct is valid.</p>

<h2>3. Small Code Example (Traits)</h2>
<pre><code class="language-rust">// Defining the contract
trait Led {
    fn turn_on(&mut self);
}

// A generic function with a Trait Bound
// It accepts ANY hardware that implements the Led trait!
fn alert_user(indicator: &mut impl Led) {
    indicator.turn_on();
}
</code></pre>

<h2>4. Embedded Firmware Example (Lifetimes)</h2>
<p>If you want to create a struct that holds a borrowed view of a sensor's data buffer, you must annotate it with a lifetime <code>'a</code>.</p>
<pre><code class="language-rust">// The struct cannot outlive the data it points to!
struct SensorBuffer<'a> {
    data_slice: &'a [u8], 
}

fn main() {
    let raw_data = [10, 20, 30]; // Lives in main
    let buffer = SensorBuffer { data_slice: &raw_data }; // Safe!
}
</code></pre>

<h2>5. Recap</h2>
<p>Traits define shared behavior contracts (methods). You can use Trait Bounds to write generic, reusable code. Lifetimes (`'a`) are annotations that tell the compiler how long a reference is valid, preventing dangling pointers. Lifetimes are mostly inferred, but must be explicit in structs holding references.</p>

<h2>6. Common Mistakes Beginners Make</h2>
<ul>
    <li>Thinking they need to write explicit lifetimes everywhere. (You don't! The compiler infers 95% of them in functions).</li>
    <li>Confusing Traits with Classes. Traits only hold methods, not data.</li>
</ul>
"""
cha4 = """
<ol>
    <li><strong>Challenge 1:</strong> Define a trait called `Sensor` with a method `read_data(&self) -> u32;`.</li>
    <li><strong>Challenge 2:</strong> Explain why storing a reference inside a `struct` requires a lifetime annotation like `<'a>`.</li>
</ol>
"""
ass4 = """
<p><strong>Assignment Idea:</strong> Write a struct `UartDevice<'a>` that holds an immutable reference to a `String` representing its configuration. Ensure the syntax compiles.</p>
"""
mcq4 = """
<ol>
    <li><strong>MCQ 1:</strong> What does a Trait define in Rust? <br><em>(A) Data layout (B) Behavior contracts/methods (C) Memory size</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 2:</strong> What is the syntax for a generic function parameter bounded by a Trait? <br><em>(A) item: impl TraitName (B) item: extends TraitName (C) item: TraitName</em><br><strong>Answer: A</strong></li>
    <li><strong>MCQ 3:</strong> What do Lifetimes mathematically prevent? <br><em>(A) Stack Overflows (B) Dangling Pointers (C) Type Mismatches</em><br><strong>Answer: B</strong></li>
    <li><strong>MCQ 4:</strong> True or False: You must explicitly write lifetime annotations `<'a>` for every single function that takes a reference. <br><strong>Answer: False</strong> (Rust uses lifetime elision to infer most of them).</li>
    <li><strong>MCQ 5:</strong> Why is the `embedded-hal` heavily reliant on Traits? <br><em>(A) To allow hardware-agnostic drivers to be written once (B) Because Traits are faster than functions (C) To save memory</em><br><strong>Answer: A</strong></li>
</ol>
"""
process_and_save(l4, exp4, cha4, ass4, mcq4)

print("Module 2 rewritten with Beginner-Friendly content!")
