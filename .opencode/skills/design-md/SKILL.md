---
name: design-md
description: Create a DESIGN.md file for any project following the Google Stitch and awesome-design-md conventions. Load this skill when the user asks to generate, scaffold, or update a DESIGN.md.
---

## What I do

Generate a `DESIGN.md` file that defines a project's design system — colors, typography, spacing, components, layout, and visual rules — using the [Google Stitch DESIGN.md specification](https://stitch.withgoogle.com/docs/design-md/specification/) format.

## When to use me

Use this when the user wants to:
- Create a DESIGN.md for their project
- Document their UI/design system in a standard format
- Set up a design reference for AI coding agents to generate consistent UI

## Workflow

1. **Ask the user** about their project's visual style — brand colors, typography preferences, design influences, target platforms (web, mobile, etc.).
2. **Generate** a DESIGN.md following the template below.
3. **Write** the file to the project root as `DESIGN.md`.

## Template

Generate a `DESIGN.md` with this structure:

### Frontmatter (YAML)

```yaml
---
version: alpha
name: <project-name>-design
description: <brief description of the design language>

colors:
  primary: "<hex>"
  on-primary: "<hex>"
  canvas: "<hex>"
  # add all semantic color tokens

typography:
  fontFamily: "<family>"
  display-xl:
    fontFamily: "<family>"
    fontSize: <px>
    fontWeight: <number>
    lineHeight: <px>
    letterSpacing: <px>
  body-md:
    fontFamily: "<family>"
    fontSize: <px>
    fontWeight: <number>
    lineHeight: <px>
  # add all type tokens (display, body, caption, code, button)

spacing:
  xs: <px>
  sm: <px>
  md: <px>
  lg: <px>
  xl: <px>
  # 4px or 8px base unit recommended

rounded:
  none: 0px
  sm: <px>
  md: <px>
  lg: <px>
  full: 9999px

components:
  button-primary:
    backgroundColor: "{}"
    textColor: "{}"
    rounded: "{}"
    typography: "{}"
    padding: "<px> <px>"
  # define all key components with token references
---
```

### Markdown sections

1. **Overview** — describe the design philosophy, mood, character in 2-4 sentences
2. **Colors** — document each color token with hex, role, and usage guidance
3. **Typography** — font stack, type scale table (token, size, weight, line-height, use case), any special rules (tracking, case)
4. **Layout & Spacing** — grid system, max-width, spacing scale, whitespace philosophy
5. **Shapes & Elevation** — border radius scale, shadow system, surface hierarchy
6. **Components** — key component patterns (buttons, cards, inputs, nav) with styling properties
7. **Do's and Don'ts** — 3-5 design guardrails per category
