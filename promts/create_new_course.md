# Consolidated Master Prompt for Building Any Course on the Platform

Use this prompt as the **base instruction** whenever creating a new course for the platform. Then append a small course-specific prompt for the subject, level, syllabus, and evaluation rules.

***

## Master Prompt

Build a rich, AI-first, gamified self-learning course experience for an online learning platform where students can learn independently without needing to leave the platform for explanations, practice, or evaluation. The platform should combine structured teaching, interactive challenges, gamification, and instant AI feedback in a way that keeps learners engaged and progressing.

The course must be designed so that a student can:
- Learn each topic through clear explanations.
- Practice immediately after learning.
- Attempt MCQs, coding challenges, assignments, and mini-projects.
- Submit answers and receive instant AI evaluation.
- Get guided suggestions for improvement.
- Progress through gamified milestones, rewards, and mastery tracking.

The experience should feel like a combination of:
- interactive teaching,
- challenge-based learning,
- AI tutoring,
- instant review and rating,
- and game-like progression.

***

## Product Vision

The platform is a self-learning system focused on deep engagement and independent mastery. It should minimize the learner's need to use outside tools by embedding explanation, examples, challenges, feedback, and revision guidance into one continuous flow.

The course should be optimized for:
- beginner to advanced learning,
- high learner engagement,
- repeatable course creation at scale,
- low-cost course delivery,
- AI-assisted evaluation,
- and measurable skill progression.

***

## Course Structure Requirements

For every course, create a complete learning flow with the following structure:

1. **Course overview**
   - Course title
   - Short description
   - Learning outcomes
   - Skill level
   - Duration estimate
   - Prerequisites
   - Tags/category

2. **Module structure**
   - Divide the course into modules.
   - Each module should contain multiple lessons.
   - Each lesson should be short, focused, and progressive.

3. **Per-lesson learning flow**
   For each lesson, include:
   - Concept explanation
   - Simple example
   - Visual or intuitive explanation when relevant
   - Quick recap
   - Knowledge check
   - Practice task
   - Hint system
   - AI feedback hooks

4. **Assessment structure**
   Every module should contain:
   - MCQs
   - Short-answer questions
   - Hands-on challenge
   - Assignment or coding task
   - Optional mini-project

5. **Completion structure**
   - Module completion rules
   - XP or point reward
   - Badge or milestone unlock
   - Readiness score or mastery score

***

## Teaching Style Requirements

The platform should teach in a way that is:
- clear,
- friendly,
- practical,
- progressive,
- and motivating.

For each concept:
- explain what it is,
- explain why it matters,
- explain where it is used,
- show a small example,
- then move to learner action.

The system should avoid passive reading-only teaching. Every major concept should lead quickly into an interaction, question, or challenge.

Use a style that reduces dependency on external AI tools:
- give strong explanations inside the lesson,
- provide contextual hints,
- provide step-by-step nudges,
- provide correction suggestions,
- but avoid instantly giving full solutions unless explicitly allowed.

***

## Gamification Requirements

Include strong gamification features in every course experience.

### Core gamification elements
- XP points for lesson completion, quiz performance, and assignment quality.
- Levels that reflect learning progression.
- Streak tracking for daily or weekly engagement.
- Badges for milestones, consistency, accuracy, and challenge completion.
- Locked and unlocked modules based on progression.
- Progress map that shows journey status.
- Missions or quests instead of only plain lesson lists.
- Daily challenge and weekly challenge options.
- Boss challenge at the end of major modules.

### Motivation design
- Reward consistency.
- Reward improvement, not only perfect answers.
- Show progress visually.
- Encourage retry with limits.
- Give mastery feedback at topic level.
- Make the learner feel they are advancing through a meaningful path.

***

## AI Evaluation Requirements

All learner submissions should be evaluated by AI instantly wherever possible.

### Submission types to evaluate
- MCQs
- Short answers
- Descriptive answers
- Coding exercises
- Assignments
- Mini-project submissions

### AI evaluation behavior
For each submission, the AI should provide:
- score or rating,
- correctness review,
- concept understanding review,
- strengths,
- mistakes,
- improvement suggestions,
- next-step recommendation,
- mastery estimate.

### AI feedback style
Feedback should be:
- immediate,
- constructive,
- specific,
- encouraging,
- and actionable.

It should not only say right or wrong. It should explain why, what is missing, and how to improve.

### Evaluation dimensions
Depending on the assignment type, score using some or all of these:
- correctness,
- clarity,
- completeness,
- logic,
- code quality,
- efficiency,
- creativity,
- formatting,
- concept coverage,
- communication quality.

### Rating output
Return a structured result such as:
- numeric score,
- star rating,
- mastery band,
- pass/fail/retry needed,
- confidence or quality label.

***

## Submission Control Requirements

Submissions should not be unlimited by default.

For each assessment item, support:
- attempt limits,
- cooldown periods,
- retry rules,
- partial penalty for repeated attempts,
- AI token usage limits,
- escalation from hint to stronger hint to review mode.

The platform should encourage thoughtful submission rather than random repeated attempts.

Suggested policy support:
- fixed number of attempts per challenge,
- extra attempts unlocked by XP or instructor/admin rules,
- separate practice mode and graded mode,
- retry after reviewing AI feedback.

***

## Unique Platform Differentiators

Ensure the course design reflects these differentiators:

1. **No-need-to-leave learning flow**
   The learner should get explanation, practice, challenge, evaluation, and revision inside one product experience.

2. **AI as evaluator and coach**
   AI should not only grade, but also guide, diagnose weak areas, and suggest the next best action.

3. **Adaptive challenge difficulty**
   The system should be able to increase or decrease challenge difficulty based on learner performance.

4. **Topic-level mastery graph**
   Track mastery by concept, not just by course completion.

5. **Submission economy**
   Learners should treat attempts as valuable. Limit retries intelligently and use them as part of motivation design.

6. **Gamified self-learning journey**
   The course should feel like a progression system rather than a static content library.

7. **Action-oriented lessons**
   Every lesson should lead quickly into a learner action.

8. **Integrated remediation**
   If a learner performs poorly, the system should recommend review lessons, easier practice, or prerequisite refreshers.

***

## Feature List to Include in Every Course Design

### Learner-facing features
- Course dashboard
- Module roadmap
- Lesson player
- Interactive coding/practice workspace
- Hint system
- MCQ engine
- Assignment submission flow
- AI evaluation panel
- Progress tracker
- XP and level system
- Badge display
- Streak tracker
- Mastery map
- Revision queue
- Retry and attempt tracker
- Achievement notifications
- Leaderboard or cohort ranking
- Certificate or completion badge

### Assessment features
- MCQs with explanations
- Scenario questions
- Coding challenges
- Assignments
- Mini-projects
- Hidden and visible test cases where relevant
- Rubric-based grading
- AI comments
- Suggested correction path
- Retry recommendation

### Personalization features
- Adaptive next lesson recommendation
- Weak-topic recommendations
- Personalized revision queue
- Difficulty tuning
- Suggested practice path
- Daily learning target

### Instructor/admin/platform features
- Course builder
- Module and lesson editor
- Quiz and assignment builder
- Rubric configuration
- Attempt limit configuration
- AI evaluation policy settings
- Difficulty controls
- Badge and XP configuration
- Learner analytics dashboard
- Cohort performance dashboard
- Submission audit trail
- Content publishing workflow

***

## Content Design Rules

Whenever creating the actual course content:
- Keep lessons short and focused.
- Use examples before complexity.
- Move from basic to advanced gradually.
- Add practice immediately after explanation.
- Add recap after each lesson.
- Add challenge after each major topic.
- Use plain language first, then technical precision.
- Design for engagement, not only syllabus coverage.

For programming courses specifically:
- Include explanation of syntax and logic.
- Show worked examples.
- Provide code tracing exercises.
- Add debugging tasks.
- Add output prediction questions.
- Add challenge-based exercises.
- Add assignments with AI review.
- Add style and efficiency suggestions in evaluation.

***

## Output Format Requirements

Whenever this prompt is used to generate a course, structure the output in this order:

1. Course summary
2. Learner persona and prerequisites
3. Learning outcomes
4. Full module breakdown
5. Lesson-by-lesson structure
6. Assessment design
7. Gamification design
8. AI evaluation design
9. Submission policy
10. Unique platform behavior for this course
11. Learner journey from onboarding to completion
12. Admin/instructor controls needed
13. MVP features for this course
14. Advanced features for future version

***

## Reusable Add-On Prompt Template

After the master prompt above, append a small course-specific prompt in this format:

### Course-specific add-on
- Course name:
- Subject/domain:
- Target learners:
- Skill level:
- Course duration:
- Number of modules:
- Required topics:
- Required assignment types:
- Evaluation strictness:
- Attempt limit policy:
- Tone/style preference:
- Any special gamification needs:
- Any project or capstone requirement:

***

## Example Add-On

### Course-specific add-on
- Course name: Python Programming for Beginners
- Subject/domain: Python programming
- Target learners: students and beginners with no prior coding background
- Skill level: beginner
- Course duration: 8 weeks
- Number of modules: 10
- Required topics: variables, data types, operators, loops, functions, lists, dictionaries, file handling, OOP basics, mini project
- Required assignment types: MCQs, coding exercises, debugging tasks, mini project
- Evaluation strictness: medium
- Attempt limit policy: 3 graded attempts per challenge, unlimited practice mode
- Tone/style preference: beginner-friendly, motivating, practical
- Any special gamification needs: daily coding streak and boss challenge after every 2 modules
- Any project or capstone requirement: build a small CLI-based student utility project

***

## One-Line Usage Instruction

Use the **Master Prompt** as the foundation for every course on the platform, then append the **Course-specific add-on** for the exact subject you want to create.