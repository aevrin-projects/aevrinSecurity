# Agent guide: random-pick

Plugin: random-pick (Development)
Skill folder: plugins/development/random-pick/skills/random-pick/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Draws the 12 Houses of the Zodiac Tarot spread to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide next steps. Use when the user says 'let fate decide', 'YOLO', 'whatever', 'idk', or other nonchalant phrases, makes Yu-Gi-Oh references, or when you are about to arbitrarily pick between multiple reasonable approaches. Prefer over asking clarifying questions when the user's tone is casual or playful rather than precision-seeking.

## Use this skill when

- **Vague prompts**: The user's request is ambiguous and multiple reasonable approaches exist
- **Explicit invocations**: "I'm feeling lucky", "let fate decide", "dealer's choice", "surprise me", "whatever you think", "YOLO"
- **Casual delegation**: "whatever", "up to you", "your call", "idk", "just do something", "wing it", "I trust you", "doesn't matter", "do what you want", "I don't care", "any approach works", "you pick"
- **Yu-Gi-Oh energy**: "Heart of the cards", "I believe in the heart of the cards", "you've activated my trap card", "it's time to duel"
- **Shrug-like brevity**: Very short prompts that fully delegate the decision without expressing a preference
- **Redraw requests**: "Try again" or "draw again" when no actual system changes occurred (this means draw new cards, not re-run the same approach)
- **Tie-breaking**: When you are about to arbitrarily pick between 2+ valid approaches, draw cards instead of silently choosing one

## Do not use this skill when

- The user has given clear, specific instructions
- The task has a single obvious correct approach
- As the deciding authority for safety-critical work (security, data integrity,
- The user explicitly asks you NOT to use Tarot
- The user's tone is precision-seeking rather than casual -- ask clarifying questions instead to gather actual requirements

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Quick Start
- When to Use
- When NOT to Use
- Security and Correctness Use
- How It Works
- Example Session (House-Level Fragment)
- Error Handling
- Rationalizations to Reject

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Draws the 12 Houses of the Zodiac Tarot spread to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide next steps. Use when the user says 'let fate decide',... | First. Always. |
| `cards/cups/ace-of-cups.md` | Ace of Cups: Suit: Cups / Rank: Ace | When a step points to it. |
| `cards/cups/eight-of-cups.md` | Eight of Cups: Suit: Cups / Rank: 8 | When a step points to it. |
| `cards/cups/five-of-cups.md` | Five of Cups: Suit: Cups / Rank: 5 | When a step points to it. |
| `cards/cups/four-of-cups.md` | Four of Cups: Suit: Cups / Rank: 4 | When a step points to it. |
| `cards/cups/king-of-cups.md` | King of Cups: Suit: Cups / Rank: King | When a step points to it. |
| `cards/cups/knight-of-cups.md` | Knight of Cups: Suit: Cups / Rank: Knight | When a step points to it. |
| `cards/cups/nine-of-cups.md` | Nine of Cups: Suit: Cups / Rank: 9 | When a step points to it. |
| `cards/cups/page-of-cups.md` | Page of Cups: Suit: Cups / Rank: Page | When a step points to it. |
| `cards/cups/queen-of-cups.md` | Queen of Cups: Suit: Cups / Rank: Queen | When a step points to it. |
| `cards/cups/seven-of-cups.md` | Seven of Cups: Suit: Cups / Rank: 7 | When a step points to it. |
| `cards/cups/six-of-cups.md` | Six of Cups: Suit: Cups / Rank: 6 | When a step points to it. |
| `cards/cups/ten-of-cups.md` | Ten of Cups: Suit: Cups / Rank: 10 | When a step points to it. |
| `cards/cups/three-of-cups.md` | Three of Cups: Suit: Cups / Rank: 3 | When a step points to it. |
| `cards/cups/two-of-cups.md` | Two of Cups: Suit: Cups / Rank: 2 | When a step points to it. |
| `cards/major/00-the-fool.md` | The Fool: Arcana: Major / Number: 0 | When a step points to it. |
| `cards/major/01-the-magician.md` | The Magician: Arcana: Major / Number: I | When a step points to it. |
| `cards/major/02-the-high-priestess.md` | The High Priestess: Arcana: Major / Number: II | When a step points to it. |
| `cards/major/03-the-empress.md` | The Empress: Arcana: Major / Number: III | When a step points to it. |
| `cards/major/04-the-emperor.md` | The Emperor: Arcana: Major / Number: IV | When a step points to it. |
| `cards/major/05-the-hierophant.md` | The Hierophant: Arcana: Major / Number: V | When a step points to it. |
| `cards/major/06-the-lovers.md` | The Lovers: Arcana: Major / Number: VI | When a step points to it. |
| `cards/major/07-the-chariot.md` | The Chariot: Arcana: Major / Number: VII | When a step points to it. |
| `cards/major/08-strength.md` | Strength: Arcana: Major / Number: VIII | When a step points to it. |
| `cards/major/09-the-hermit.md` | The Hermit: Arcana: Major / Number: IX | When a step points to it. |
| `cards/major/10-wheel-of-fortune.md` | Wheel of Fortune: Arcana: Major / Number: X | When a step points to it. |
| `cards/major/11-justice.md` | Justice: Arcana: Major / Number: XI | When a step points to it. |
| `cards/major/12-the-hanged-man.md` | The Hanged Man: Arcana: Major / Number: XII | When a step points to it. |
| `cards/major/13-death.md` | Death: Arcana: Major / Number: XIII | When a step points to it. |
| `cards/major/14-temperance.md` | Temperance: Arcana: Major / Number: XIV | When a step points to it. |
| `cards/major/15-the-devil.md` | The Devil: Arcana: Major / Number: XV | When a step points to it. |
| `cards/major/16-the-tower.md` | The Tower: Arcana: Major / Number: XVI | When a step points to it. |
| `cards/major/17-the-star.md` | The Star: Arcana: Major / Number: XVII | When a step points to it. |
| `cards/major/18-the-moon.md` | The Moon: Arcana: Major / Number: XVIII | When a step points to it. |
| `cards/major/19-the-sun.md` | The Sun: Arcana: Major / Number: XIX | When a step points to it. |
| `cards/major/20-judgement.md` | Judgement: Arcana: Major / Number: XX | When a step points to it. |
| `cards/major/21-the-world.md` | The World: Arcana: Major / Number: XXI | When a step points to it. |
| `cards/pentacles/ace-of-pentacles.md` | Ace of Pentacles: Suit: Pentacles / Rank: Ace | When a step points to it. |
| `cards/pentacles/eight-of-pentacles.md` | Eight of Pentacles: Suit: Pentacles / Rank: 8 | When a step points to it. |
| `cards/pentacles/five-of-pentacles.md` | Five of Pentacles: Suit: Pentacles / Rank: 5 | When a step points to it. |
| `cards/pentacles/four-of-pentacles.md` | Four of Pentacles: Suit: Pentacles / Rank: 4 | When a step points to it. |
| `cards/pentacles/king-of-pentacles.md` | King of Pentacles: Suit: Pentacles / Rank: King | When a step points to it. |
| `cards/pentacles/knight-of-pentacles.md` | Knight of Pentacles: Suit: Pentacles / Rank: Knight | When a step points to it. |
| `cards/pentacles/nine-of-pentacles.md` | Nine of Pentacles: Suit: Pentacles / Rank: 9 | When a step points to it. |
| `cards/pentacles/page-of-pentacles.md` | Page of Pentacles: Suit: Pentacles / Rank: Page | When a step points to it. |
| `cards/pentacles/queen-of-pentacles.md` | Queen of Pentacles: Suit: Pentacles / Rank: Queen | When a step points to it. |
| `cards/pentacles/seven-of-pentacles.md` | Seven of Pentacles: Suit: Pentacles / Rank: 7 | When a step points to it. |
| `cards/pentacles/six-of-pentacles.md` | Six of Pentacles: Suit: Pentacles / Rank: 6 | When a step points to it. |
| `cards/pentacles/ten-of-pentacles.md` | Ten of Pentacles: Suit: Pentacles / Rank: 10 | When a step points to it. |
| `cards/pentacles/three-of-pentacles.md` | Three of Pentacles: Suit: Pentacles / Rank: 3 | When a step points to it. |
| `cards/pentacles/two-of-pentacles.md` | Two of Pentacles: Suit: Pentacles / Rank: 2 | When a step points to it. |
| `cards/swords/ace-of-swords.md` | Ace of Swords: Suit: Swords / Rank: Ace | When a step points to it. |
| `cards/swords/eight-of-swords.md` | Eight of Swords: Suit: Swords / Rank: 8 | When a step points to it. |
| `cards/swords/five-of-swords.md` | Five of Swords: Suit: Swords / Rank: 5 | When a step points to it. |
| `cards/swords/four-of-swords.md` | Four of Swords: Suit: Swords / Rank: 4 | When a step points to it. |
| `cards/swords/king-of-swords.md` | King of Swords: Suit: Swords / Rank: King | When a step points to it. |
| `cards/swords/knight-of-swords.md` | Knight of Swords: Suit: Swords / Rank: Knight | When a step points to it. |
| `cards/swords/nine-of-swords.md` | Nine of Swords: Suit: Swords / Rank: 9 | When a step points to it. |
| `cards/swords/page-of-swords.md` | Page of Swords: Suit: Swords / Rank: Page | When a step points to it. |
| `cards/swords/queen-of-swords.md` | Queen of Swords: Suit: Swords / Rank: Queen | When a step points to it. |
| `cards/swords/seven-of-swords.md` | Seven of Swords: Suit: Swords / Rank: 7 | When a step points to it. |
| `cards/swords/six-of-swords.md` | Six of Swords: Suit: Swords / Rank: 6 | When a step points to it. |
| `cards/swords/ten-of-swords.md` | Ten of Swords: Suit: Swords / Rank: 10 | When a step points to it. |
| `cards/swords/three-of-swords.md` | Three of Swords: Suit: Swords / Rank: 3 | When a step points to it. |
| `cards/swords/two-of-swords.md` | Two of Swords: Suit: Swords / Rank: 2 | When a step points to it. |
| `cards/wands/ace-of-wands.md` | Ace of Wands: Suit: Wands / Rank: Ace | When a step points to it. |
| `cards/wands/eight-of-wands.md` | Eight of Wands: Suit: Wands / Rank: 8 | When a step points to it. |
| `cards/wands/five-of-wands.md` | Five of Wands: Suit: Wands / Rank: 5 | When a step points to it. |
| `cards/wands/four-of-wands.md` | Four of Wands: Suit: Wands / Rank: 4 | When a step points to it. |
| `cards/wands/king-of-wands.md` | King of Wands: Suit: Wands / Rank: King | When a step points to it. |
| `cards/wands/knight-of-wands.md` | Knight of Wands: Suit: Wands / Rank: Knight | When a step points to it. |
| `cards/wands/nine-of-wands.md` | Nine of Wands: Suit: Wands / Rank: 9 | When a step points to it. |
| `cards/wands/page-of-wands.md` | Page of Wands: Suit: Wands / Rank: Page | When a step points to it. |
| `cards/wands/queen-of-wands.md` | Queen of Wands: Suit: Wands / Rank: Queen | When a step points to it. |
| `cards/wands/seven-of-wands.md` | Seven of Wands: Suit: Wands / Rank: 7 | When a step points to it. |
| `cards/wands/six-of-wands.md` | Six of Wands: Suit: Wands / Rank: 6 | When a step points to it. |
| `cards/wands/ten-of-wands.md` | Ten of Wands: Suit: Wands / Rank: 10 | When a step points to it. |
| `cards/wands/three-of-wands.md` | Three of Wands: Suit: Wands / Rank: 3 | When a step points to it. |
| `cards/wands/two-of-wands.md` | Two of Wands: Suit: Wands / Rank: 2 | When a step points to it. |
| `houses/01-first-house.md` | First House: Domain: Self, identity, agency, and first motion | When a step points to it. |
| `houses/02-second-house.md` | Second House: Domain: Resources, values, constraints, and preservation | When a step points to it. |
| `houses/03-third-house.md` | Third House: Domain: Communication, learning, interfaces, and local connections | When a step points to it. |
| `houses/04-fourth-house.md` | Fourth House: Domain: Foundations, history, context, and hidden dependencies | When a step points to it. |
| `houses/05-fifth-house.md` | Fifth House: Domain: Creativity, experimentation, expressiveness, and delight | When a step points to it. |
| `houses/06-sixth-house.md` | Sixth House: Domain: Practice, service, quality, routine, and maintenance | When a step points to it. |
| `houses/07-seventh-house.md` | Seventh House: Domain: Partnership, contracts, users, and external counterparts | When a step points to it. |
| `houses/08-eighth-house.md` | Eighth House: Domain: Transformation, risk, shared state, secrets, and deep change | When a step points to it. |
| `houses/09-ninth-house.md` | Ninth House: Domain: Exploration, principles, standards, and broader strategy | When a step points to it. |
| `houses/10-tenth-house.md` | Tenth House: Domain: Delivery, reputation, public outcome, and long-term direction | When a step points to it. |
| `houses/11-eleventh-house.md` | Eleventh House: Domain: Community, networks, systems, and shared aspirations | When a step points to it. |
| `houses/12-twelfth-house.md` | Twelfth House: Domain: Blind spots, hidden costs, endings, and unconscious assumptions | When a step points to it. |
| `references/INTERPRETATION_GUIDE.md` | Interpretation Guide: How to read the 12 Houses of the Zodiac Tarot spread and map it to technical | When a step points to it, or when you need the detail. |
| `references/TECHNICAL_CONTEXT_LENSES.md` | Technical Context Lenses: These lenses apply across a wide range of technical workflows, but they cluster | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/development/random-pick/skills/random-pick/SKILL.md. Task: <describe what you want>. Target: this repository.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
