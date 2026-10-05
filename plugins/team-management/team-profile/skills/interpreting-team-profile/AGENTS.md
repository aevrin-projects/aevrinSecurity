# Agent guide: interpreting-team-profile

Plugin: team-profile (Team Management)
Skill folder: plugins/team-management/team-profile/skills/interpreting-team-profile/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Interprets Team Profile (CI) surveys, behavioral profiles, and personality assessment data. Supports individual profile interpretation, team composition analysis (gas/brake/glue), burnout detection, profile comparison, hiring profiles, manager coaching, interview transcript analysis for trait prediction, candidate debrief, onboarding planning, and conflict mediation. Accepts extracted JSON or PDF input via OpenCV extraction script. Use when the user shares a Team Profile PDF or JSON profile, asks what someone's CI traits mean, compares Team Profile profiles across a team or against a hiring profile, or asks about burnout risk from Survey-versus-Job gaps.

## Use this skill when

- Interpreting Team Profile survey results (individual or team)
- Analyzing CI profiles from PDF or JSON data
- Assessing team composition using Gas/Brake/Glue framework
- Detecting burnout risk by comparing Survey vs Job graphs
- Defining hiring profiles based on CI trait patterns
- Coaching managers on how to work with specific CI profiles
- Predicting CI traits from interview transcripts

## Do not use this skill when

- For non-CI behavioral assessments (DISC, Myers-Briggs, StrengthsFinder, Predictive Index, Enneagram)
- For clinical psychological assessments or diagnoses
- As the sole basis for hiring/firing decisions - CI is one data point among many
- Check same directory as PDF for `.json` file with matching name
- Check if user provided JSON path
- **CI Survey JSON** → Proceed to Step 2
- **CI Survey PDF** → Extract first (Step 0), then proceed to Step 2

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Interprets Team Profile (CI) surveys, behavioral profiles, and personality assessment data. Supports individual profile interpretation, team composition analysis (gas/brake/glue), burnout detection, profile comparison, hiring... | First. Always. |
| `references/anti-patterns.md` | Common mistakes when interpreting Team Profile profiles. Avoiding these errors is as important as understanding the methodology itself. | When a step points to it, or when you need the detail. |
| `references/archetype-administrator.md` | The Administrator (High A, High B, Low C, Mid D): Core: Reasonably proactive, impatient, and amiable communicator. Not strong in the analytical sense, but has the ability to "read" people and situations effectively. Outgoing,... | When a step points to it, or when you need the detail. |
| `references/archetype-coordinator.md` | The Coordinator (Low A, High B, Mid C, Low D): Core: Optimistic, persuasive, socially oriented task facilitator. Sounds assertive and take-charge but is actually an amicable, friendly coordinator who prefers being the... | When a step points to it, or when you need the detail. |
| `references/archetype-craftsman.md` | The Craftsman (Low A, Low B, High C, High D): Core: Reactive, routine-oriented, and deeply focused on a single task or trade. Gravitates toward the familiar and avoids perceived risk. Predictable, consistent, and highly... | When a step points to it, or when you need the detail. |
| `references/archetype-daredevil.md` | The Daredevil (High A, Low B, Low C, Low D): Core: Independent, autonomous, take-charge personality with a "No-Fear" mentality. Craves freedom from society, rules, structure, and conformity. Unconventional and uninhibited free... | When a step points to it, or when you need the detail. |
| `references/archetype-debater.md` | The Debater (Mid A, Mid-High B, Low C, High D): Core: Reasonably assertive and approachable. A friendly, somewhat relaxed person who naturally gravitates to social circles to exchange ideas. Persuasive communicator, usually at... | When a step points to it, or when you need the detail. |
| `references/archetype-facilitator.md` | The Facilitator (Low A, Mid B, Mid C, Low D): Core: Polite, cordial, and initially guarded but warms up over time. Easy going and deliberate, excels at single-focus tasks executed in a systematic, methodical way. Socially... | When a step points to it, or when you need the detail. |
| `references/archetype-influencer.md` | The Influencer (Low A, High B, Low C, Low D): Core: Open, optimistic, unselfish. Comfortable in support roles involving people, service and tasks. Altruistic - finds it hard to say no. Need not to disappoint often puts them... | When a step points to it, or when you need the detail. |
| `references/archetype-operator.md` | The Operator (Low A, Low B, High C, Mid-High D): Core: Easy going, laid back processor of tasks. A creature of habit who prefers stability and predictability. Not a change agent - as steady and consistent as you can get for an... | When a step points to it, or when you need the detail. |
| `references/archetype-persuader.md` | The Persuader (High A, High B, Low C, Low D): Core: Proactive, impatient, charismatic communicator. Not strong analytically but has the ability to "read" people and situations effectively. Outgoing, empathetic, and intuitive.... | When a step points to it, or when you need the detail. |
| `references/archetype-philosopher.md` | The Philosopher (Low A, Low B, High C, Low D): Core: Independent, cerebral, idea-driven. Research persistent, strives to stay in a thinking and imaginative environment. A true "ideas" person - out-of-the-box thinking at its... | When a step points to it, or when you need the detail. |
| `references/archetype-rainmaker.md` | The Rainmaker (High A, High B, Low C, Low D): Core: Assertive, outgoing, socially oriented. Uncanny ability to "read" people despite weak analytical skills. Thrives on putting deals together and has fun doing it. | When a step points to it, or when you need the detail. |
| `references/archetype-scholar.md` | The Scholar (High A, Low B, Low C, High D): Core: Somewhat proactive, independent, and research-persistent. Respected for deep knowledge, single focus, and attention span. Relies on information and data from past situations to... | When a step points to it, or when you need the detail. |
| `references/archetype-socializer.md` | The Socializer (Low A, High B, Low C, Low D): Core: Socially flamboyant, people-oriented, and empathetic. Thrives in environments where they can meet, greet, and build relationships. Needs to be seen, heard, and liked - people... | When a step points to it, or when you need the detail. |
| `references/archetype-specialist.md` | The Specialist (Low A, Low B, High C, Mid D): Core: Private, guarded, and introspective. Cannot sit down to watch a movie or relax with friends without a sense of guilt that "there is so much I haven't finished today." Driven... | When a step points to it, or when you need the detail. |
| `references/archetype-technical-expert.md` | The Technical Expert (Low A, Low B, High C, Low D): Core: Impatient, reasonably proactive person who excels in their area of expertise. Driven to be accurate, they will demonstrate their knowledge when given opportunities to... | When a step points to it, or when you need the detail. |
| `references/archetype-traditionalist.md` | The Traditionalist (Low A, Low B, High C, High D): Core: Reactive, diligent, detail-oriented individual who draws strength from knowledge and past events. Experts at recalling historic events, people, times, and places.... | When a step points to it, or when you need the detail. |
| `references/archetype-trailblazer.md` | The Trailblazer (High A, Mid B, Mid C, Low D): Core: Proactive, confident self-starter that thrives in competitive situations. Focused on winning and driven to be the best at work or hobbies. Tenacious and determined in... | When a step points to it, or when you need the detail. |
| `references/conversation-starters.md` | Conversation starters and engagement strategies based on Team Profile traits. Use these to build rapport, deliver feedback effectively, and engage team members based on their profile. | When a step points to it, or when you need the detail. |
| `references/interview-trait-signals.md` | This reference helps predict Team Profile traits from interview transcripts. Candidates don't take CI during interviews - these signals help estimate traits before the actual survey is administered after an offer is sign | When a step points to it, or when you need the detail. |
| `references/motivators.md` | The simplest way to drive engagement and productivity is to find the leading dot among A, B, D (the three confidence traits) and install motivators for that trait consistently. | When a step points to it, or when you need the detail. |
| `references/patterns-archetypes.md` | Team Profile identifies 19 distinct behavioral patterns based on the configuration of A, B, C, D traits. The interaction between traits reveals more than individual positions. | When a step points to it, or when you need the detail. |
| `references/primary-traits.md` | The four primary traits (A, B, C, D) are the main drivers of behavior. The relationship BETWEEN dots is often more important than individual positions. All interpretations are relative to the red arrow (population mean). | When a step points to it, or when you need the detail. |
| `references/secondary-traits.md` | Secondary traits (EU, L, I) supplement the primary traits. L and I are unique: they use absolute values and CAN be compared directly between people. | When a step points to it, or when you need the detail. |
| `references/team-composition.md` | Every team needs the right mix of Gas, Brake, and Glue for its current needs. The ratio depends on the season of business, the function, and current gaps. | When a step points to it, or when you need the detail. |
| `templates/burnout-report.md` | Burnout Detection Report Template: Copy and fill this template when analyzing burnout risk using Team Profile Survey vs Job comparison. | When you write output in that format. |
| `templates/comparison-report.md` | Profile Comparison Report Template: Copy and fill this template when comparing two Team Profile profiles for compatibility analysis. | When you write output in that format. |
| `templates/hiring-profile.md` | Hiring Profile Template: Copy and fill this template when defining the ideal Team Profile profile for a role. | When you write output in that format. |
| `templates/individual-report.md` | Individual Profile Report Template: Copy and fill this template when reporting on an individual's Team Profile profile. | When you write output in that format. |
| `templates/predicted-profile.md` | Predicted Profile Template: Copy and fill this template when predicting Team Profile traits from interview transcripts. | When you write output in that format. |
| `templates/team-report.md` | Team Composition Report Template: Copy and fill this template when analyzing team composition using Team Profile profiles. | When you write output in that format. |
| `workflows/analyze-team.md` | Read these reference files before analyzing: | At the phase it belongs to. |
| `workflows/coach-manager.md` | Read these reference files before coaching: | At the phase it belongs to. |
| `workflows/compare-profiles.md` | Read these reference files before comparing: | At the phase it belongs to. |
| `workflows/define-hiring-profile.md` | Read these reference files before defining a hiring profile: | At the phase it belongs to. |
| `workflows/detect-burnout.md` | Read these reference files before analyzing: | At the phase it belongs to. |
| `workflows/extract-from-pdf.md` | Extract from PDF Workflow: Extract Team Profile profile data from a PDF file and convert to JSON format. | At the phase it belongs to. |
| `workflows/interpret-individual.md` | Read these reference files before interpreting: | At the phase it belongs to. |
| `workflows/interview-debrief.md` | Read these reference files before debrief: | At the phase it belongs to. |
| `workflows/mediate-conflict.md` | Read these reference files before mediation: | At the phase it belongs to. |
| `workflows/plan-onboarding.md` | Read these reference files before planning onboarding: | At the phase it belongs to. |
| `workflows/predict-from-interview.md` | Read these reference files before analyzing: | At the phase it belongs to. |

## Example requests

- Use: Use plugins/team-management/team-profile/skills/interpreting-team-profile/SKILL.md. Task: <describe what you want>. Target: this repository.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
