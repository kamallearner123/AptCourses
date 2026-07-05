# AptCourses: Rust on STM32

![AptCourses Hero](static/images/hero_bg.png)

## The Motto
**"Bridging the gap between High-Level Software Engineering and Bare-Metal Hardware."**

At AptCourses, we believe that writing memory-safe, deterministic, and highly concurrent firmware shouldn't require decades of arcane C/C++ experience. Our mission is to provide an industry-grade, highly engaging pedagogical experience that empowers developers to master **Embedded Rust on STM32 Microcontrollers**. We take complex hardware concepts and break them down into visually stunning, beginner-friendly, and interactive lessons.

## About the Project
**AptCourses** is a custom-built, modern Learning Management System (LMS) powered by Django. It is specifically architected to host deep-tech engineering courses. 

Currently, the flagship course is **"Rust on STM32,"** a 20-module deep dive into bare-metal development. 

### Key Features of the Platform
- 🎨 **Modern Cyber-Aesthetic UI:** Built from the ground up with custom Glassmorphism, a dedicated Dark/Light mode engine, and responsive mobile-first layouts.
- 🦸‍♂️ **Visual Storytelling:** Every technical concept is introduced via custom, high-quality 6-panel technical comic strips (e.g., illustrating data races, panic handlers, and ESD safety) to boost engagement and retention.
- ⌨️ **Syntax-Aware Rendering:** Deep integration with PrismJS ensures that all C, C++, and Rust code blocks are beautifully and accurately syntax-highlighted.
- 🧠 **Interactive Assessments:** Features built-in, AI-ready interactive forms for Challenges and MCQs. Click-to-validate buttons and hidden answers ensure active recall.
- 📖 **Smart Navigation:** A 20-module curriculum is heavily optimized with contextual `<details>` collapsing and auto-scrolling sidebars, so you never lose your place.

## Technology Stack
- **Backend:** Python / Django / SQLite
- **Frontend:** HTML5, Vanilla CSS (Custom CSS Variables & Glassmorphism), Vanilla JavaScript
- **Syntax Engine:** PrismJS (Tomorrow Night theme)

## Getting Started

### Prerequisites
- Python 3.10+
- `pip`

### Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:kamallearner123/AptCourses.git
   cd AptCourses
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the development server (which handles migrations automatically):
   ```bash
   ./start.sh
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## Course Structure (Rust on STM32)
The flagship course covers everything from hardware safety basics to complex DMA transfers and RTOS integration:
*   **Module 1:** Introduction to the STM32 Ecosystem & Hardware Safety
*   **Module 2:** Rust Fundamentals (Variables, Ownership, Enums, Traits)
*   **Module 3:** Bare-Metal Constraints (`no_std`, Determinism, Panic Handling)
*   *(Modules 4-20 encompass Registers, Peripherals, Timers, DMA, and real-world sensor integrations).*
