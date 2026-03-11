# WRITING.md

## Purpose of This Document

### Why

This document defines the mandatory standard for AI Agents to generate and maintain high-quality `README.md` files for development projects.

It ensures:
1. Structural consistency.
2. Conceptual clarity.
3. Long-term maintainability.

### How

By enforcing four core principles:

- Diátaxis Framework  
- Golden Circle (Why → How → What)  
- Rule of Three  
- KISS Principle  

And by defining a dynamic update protocol.

### What

This document is a specification.  
AI Agents must follow it when:

- Creating a new `README.md`
- Updating an existing `README.md`
- Refactoring documentation structure

---

# 1. Core Documentation Principles

## 1.1 Diátaxis Framework (Document Type)

Every README must be classified under one primary type:

1. **Tutorial** – Learning-oriented, step-by-step.
2. **How-to Guide** – Task-oriented, problem-solving.
3. **Reference** – Information-oriented, precise specifications.
4. **Explanation** – Understanding-oriented, conceptual clarity.

The AI Agent must:

- Identify the dominant type.
- Structure the README accordingly.
- Maintain internal consistency with the chosen type.

If hybrid, one type must remain dominant.

---

## 1.2 Golden Circle Structure (Mandatory Backbone)

All README files must follow this order:

1. **WHY** – Purpose, problem, motivation.
2. **HOW** – Architecture, approach, methodology.
3. **WHAT** – Features, components, deliverables.

This order must not be reversed.

Rationale:
- Why provides meaning.
- How provides trust.
- What provides clarity.

---

## 1.3 Rule of Three

Whenever suitable, structure content in groups of three:

- Three core features.
- Three benefits.
- Three examples.
- Three architectural pillars.

Avoid excessive fragmentation.  
If more than three items are required, group logically.

---

## 1.4 KISS Principle

Keep It Simple and Structured.

Rules:

- Prefer short sentences.
- Avoid unnecessary jargon.
- Use bullets instead of dense paragraphs.
- Avoid marketing exaggeration.
- Prioritize clarity over cleverness.

Bad:
> This revolutionary platform dramatically transforms next-generation scalable ecosystems.

Better:
> This project provides a scalable platform for managing distributed systems.

---

# 2. README Global Structure Specification

The following structure is mandatory unless justified otherwise.

---

# 2.1 Title Section

# Project Name

Immediately followed by technology badges.

### Badge Rules

- Must reflect actual technologies used.
- Must use consistent color palette.
- Must use Shields.io-compatible format.
- Must remain visually coherent.

Example:

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Badges must not contradict the content.

---

# 2.2 Short Description

- 2–4 sentences.
- Express the **WHY**.
- Clear value proposition.
- KISS compliant.

Structure:
1. What problem it solves.
2. Who it serves.
3. Core value.

---

# 3. Golden Circle Section Implementation

## 3.1 WHY

Include:

- Problem statement.
- Motivation.
- Intended impact.

End with a short concluding sentence.

---

## 3.2 HOW

Include:

- Architecture overview.
- Key technical decisions.
- Methodology.

Use diagrams or code blocks when appropriate.

If step-by-step explanation is needed, structure clearly.

---

## 3.3 WHAT

Include:

- Features (grouped logically).
- Core modules.
- Deliverables.

Apply Rule of Three when possible.

---

# 4. Supporting Sections

## 4.1 Installation

Step-by-step instructions.

Example structure:

1. Clone repository.
2. Install dependencies.
3. Run project.

Avoid ambiguity.

---

## 4.2 Usage

Provide:

- Minimal example.
- Typical example.
- Advanced example (if relevant).

Keep concise.

---

## 4.3 Configuration (If Applicable)

Document:

- Environment variables.
- Required configuration files.
- Runtime parameters.

---

## 4.4 License (Mandatory)

Must include:

- License name.
- SPDX identifier.
- Link to LICENSE file.
- Short summary (2–3 sentences).

Example licenses:

- MIT
- Apache-2.0
- GPL-3.0

Example:

## License

This project is licensed under the MIT License.  
SPDX-License-Identifier: MIT  

See the LICENSE file for full details.

---

## 4.5 References / Validation (If Needed)

Include when appropriate:

- External standards.
- Academic references.
- Related documentation.
- Cross-check notes.

---

# 5. Logical Sequencing Rules

Sections must follow logical progression:

1. Context (Why)
2. Structure (How)
3. Capabilities (What)
4. Operation (Installation & Usage)
5. Governance (License)
6. Validation (References)

Each section should:

- Begin clearly.
- Progress logically.
- End with short contextual closure when necessary.

---

# 6. Dynamic README Evolution Rules

The README is a living document.

AI Agents must treat it as version-aware documentation.

---

## 6.1 Stability Requirements

The following must remain stable unless major refactor is justified:

- Title
- Badge block
- Golden Circle order
- License section
- Heading hierarchy

---

## 6.2 Update Protocol

When modifying an existing README:

1. Analyze current structure.
2. Identify outdated or incomplete sections.
3. Refactor instead of rewrite.
4. Preserve validated information.
5. Add content under existing logical sections when possible.
6. Only introduce new sections if structurally necessary.

Do not delete valuable information without justification.

---

## 6.3 Incremental Expansion

When adding new features:

- Update WHAT section.
- If architectural changes occur, update HOW.
- If purpose evolves, refine WHY without breaking narrative continuity.

Maintain conceptual integrity.

---

## 6.4 Consistency Checks After Updates

Verify:

- Golden Circle order maintained.
- Badge technologies still accurate.
- License unchanged unless intentionally modified.
- No duplicated sections.
- No broken links.
- Markdown hierarchy clean.
- Diátaxis type still consistent.

---

# 7. Validation Checklist (Mandatory)

Before finalizing a README, confirm:

- [ ] Diátaxis type identified
- [ ] Golden Circle order respected
- [ ] Rule of Three applied where suitable
- [ ] KISS respected
- [ ] Badges accurate and consistent
- [ ] License included with SPDX identifier
- [ ] Logical sequential flow maintained
- [ ] No structural regression after updates
- [ ] Markdown formatting valid

---

# 8. Output Constraints

- Markdown compliant.
- Clean heading hierarchy.
- No emojis unless explicitly required.
- No unnecessary verbosity.
- Production-ready.

---

# Conclusion

This WRITING.md defines a stable yet adaptable framework.

It ensures:

1. Conceptual clarity.
2. Structural consistency.
3. Long-term maintainability.

AI Agents must follow this specification strictly when generating or evolving any `README.md` file.
