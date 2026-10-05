# Agent guide: testing-skills plugin

Category: Code Auditing
Folder: plugins/code-auditing/testing-skills/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Skills from the Aevrin Security Application Security Testing Guide (aevrin.net)

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| address-sanitizer | Builds and runs code under AddressSanitizer to catch buffer overflows, use-after-free, and other memory errors during fuzzing or tests. Covers -fsanitize=address builds, ASAN_OPTIONS, reading the... | `skills/address-sanitizer/SKILL.md` |
| aflpp | Sets up and runs AFL++ for multi-core fuzzing of C/C++ projects built with afl-clang-fast or afl-gcc-fast. Covers instrumentation modes, parallel main and secondary campaigns, persistent mode,... | `skills/aflpp/SKILL.md` |
| atheris | Sets up and runs Atheris, the coverage-guided Python fuzzer built on libFuzzer. Covers TestOneInput harnesses, FuzzedDataProvider, instrumenting both pure Python and native C extensions, and... | `skills/atheris/SKILL.md` |
| cargo-fuzz | Sets up and runs cargo-fuzz, the standard fuzzing tool for Cargo-based Rust projects. Covers cargo fuzz init, the nightly toolchain requirement, fuzz_target! harnesses, Arbitrary-derived... | `skills/cargo-fuzz/SKILL.md` |
| constant-time-testing | Measures timing side channels in cryptographic implementations by running them, using dudect for statistical analysis and Timecop over Valgrind for dynamic tracing. Covers the formal, symbolic,... | `skills/constant-time-testing/SKILL.md` |
| coverage-analysis | Measures and interprets what a fuzzing campaign actually reaches, using llvm-cov, lcov, or a fuzzer's own coverage output. Covers baselining a new campaign, reading coverage reports, and turning... | `skills/coverage-analysis/SKILL.md` |
| fuzzing-dictionary | Builds and applies fuzzing dictionaries so a fuzzer can produce the keywords, magic bytes, and tokens a target expects. Covers extracting tokens from source, headers, binaries, and specifications,... | `skills/fuzzing-dictionary/SKILL.md` |
| fuzzing-obstacles | Patches past the barriers that stop a fuzzer making progress - checksum and hash verification, magic-value validation, time-based seeds, and other non-deterministic global state. Covers locating... | `skills/fuzzing-obstacles/SKILL.md` |
| harness-writing | Designs and improves fuzzing harnesses for C/C++ and Rust. Covers mapping raw bytes onto a target API, generating structured inputs, avoiding non-determinism and false crashes, and deciding what... | `skills/harness-writing/SKILL.md` |
| libafl | Builds custom fuzzers with LibAFL, the modular Rust fuzzing library. Covers composing observers, feedbacks, mutators, schedulers, and executors into a fuzzer for targets the standard tools do not... | `skills/libafl/SKILL.md` |
| libfuzzer | Sets up and runs libFuzzer, the coverage-guided fuzzer built into LLVM, on C/C++ code that compiles with Clang. Covers harness structure, -fsanitize=fuzzer builds, corpus and dictionary... | `skills/libfuzzer/SKILL.md` |
| ossfuzz | Enrolls a project in OSS-Fuzz, Google's free continuous fuzzing service for open source, and drives it locally. Covers project.yaml, Dockerfile and build.sh setup, the helper scripts, reproducing... | `skills/ossfuzz/SKILL.md` |
| rubyfuzz | Sets up and runs Rubyfuzz, a coverage-guided Ruby fuzzer and the only production-ready one for the language. Covers harness structure, fuzzing pure Ruby and the native C extensions in gems, and... | `skills/rubyfuzz/SKILL.md` |
| testing-guide-generator | Generates agent skills from the Aevrin Security Testing Guide (aevrin.net), analyzing guide pages and emitting SKILL.md files with the structure each skill type requires. Use when creating or... | `skills/testing-guide-generator/SKILL.md` |
| wycheproof | Validates cryptographic implementations against Project Wycheproof's test vectors, which encode known attacks and edge cases across AES, RSA, ECDSA, ECDH, and more. Covers loading test vectors,... | `skills/wycheproof/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Testing Guide Skills: Meta-skill that generates agent skills from the [Aevrin Security Application Security Testing Guide](https://aevrin.net). | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
