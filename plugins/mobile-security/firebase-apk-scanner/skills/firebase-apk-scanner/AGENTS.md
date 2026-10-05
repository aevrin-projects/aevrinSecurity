# Agent guide: firebase-apk-scanner

Plugin: firebase-apk-scanner (Mobile Security)
Skill folder: plugins/mobile-security/firebase-apk-scanner/skills/firebase-apk-scanner/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when analyzing APK files for Firebase vulnerabilities, performing mobile app security audits, or testing Firebase endpoint security. For authorized security research only.

## Use this skill when

- Auditing Android applications for Firebase security misconfigurations
- Testing Firebase endpoints extracted from APKs (Realtime Database, Firestore, Storage)
- Checking authentication security (open signup, anonymous auth, email enumeration)
- Enumerating Cloud Functions and testing for unauthenticated access
- Mobile app security assessments involving Firebase backends
- Authorized penetration testing of Firebase-backed applications

## Do not use this skill when

- Scanning apps you do not have explicit authorization to test
- Testing production Firebase projects without written permission
- When you only need to extract Firebase config without testing (use manual grep/strings instead)
- For non-Android targets (iOS, web apps) - this skill is APK-specific
- When the target app does not use Firebase

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Rationalizations to Reject
- Reference Documentation
- How to Use This Skill
- Workflow
- Scan Summary
- Extracted Configuration
- Vulnerabilities Found
- Remediation
- Manual Testing (If Scanner Fails)
- Severity Classification
- Important Guidelines

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when analyzing APK files for Firebase vulnerabilities, performing... | First. Always. |
| `references/vulnerabilities.md` | Firebase Security Vulnerability Patterns: Detailed vulnerability patterns, exploitation techniques, and audit checklists for Firebase implementations in mobile applications. | When a step points to it, or when you need the detail. |

## Example requests

- Find: Use plugins/mobile-security/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md. Scan the Android app at ./app.apk. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/mobile-security/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md. Scan the Android app at ./app.apk. Write a detailed report to ./reports/firebase-apk-scanner.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/firebase-apk-scanner.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
