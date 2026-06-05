---
version: alpha
name: <project-name>-design
description: <brief description of the design language (1-2 sentences)>

colors:
  primary: "<hex>"
  on-primary: "<hex>"
  canvas: "<hex>"
  canvas-soft: "<hex>"
  ink: "<hex>"
  body: "<hex>"
  mute: "<hex>"
  hairline: "<hex>"
  link: "<hex>"
  success: "<hex>"
  error: "<hex>"
  warning: "<hex>"

typography:
  fontFamily: "<family>, <fallback>"
  display-xl:
    fontFamily: "<family>, <fallback>"
    fontSize: <px>
    fontWeight: <number>
    lineHeight: <px>
    letterSpacing: <px>
  display-lg:
    fontFamily: "<family>, <fallback>"
    fontSize: <px>
    fontWeight: <number>
    lineHeight: <px>
    letterSpacing: <px>
  display-md:
    fontFamily: "<family>, <fallback>"
    fontSize: <px>
    fontWeight: <number>
    lineHeight: <px>
    letterSpacing: <px>
  body-lg:
    fontFamily: "<family>, <fallback>"
    fontSize: <px>
    fontWeight: <number>
    lineHeight: <px>
    letterSpacing: <px>
  body-md:
    fontFamily: "<family>, <fallback>"
    fontSize: <px>
    fontWeight: <number>
    lineHeight: <px>
  body-sm:
    fontFamily: "<family>, <fallback>"
    fontSize: <px>
    fontWeight: <number>
    lineHeight: <px>
  caption:
    fontFamily: "<family>, <fallback>"
    fontSize: <px>
    fontWeight: <number>
    lineHeight: <px>
  code:
    fontFamily: "<mono-family>, <mono-fallback>"
    fontSize: <px>
    fontWeight: <number>
    lineHeight: <px>
    letterSpacing: <px>
  button:
    fontFamily: "<family>, <fallback>"
    fontSize: <px>
    fontWeight: <number>
    lineHeight: <px>

spacing:
  xxs: <px>
  xs: <px>
  sm: <px>
  md: <px>
  lg: <px>
  xl: <px>
  2xl: <px>
  3xl: <px>
  4xl: <px>
  5xl: <px>
  section: <px>

rounded:
  none: 0px
  xs: <px>
  sm: <px>
  md: <px>
  lg: <px>
  xl: <px>
  pill: <px>
  full: 9999px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
    typography: "{typography.button}"
    padding: "<px> <px>"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.pill}"
    typography: "{typography.button}"
    padding: "<px> <px>"
  card-default:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  form-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "<px> <px>"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: <px>
    padding: "{spacing.sm} {spacing.lg}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    padding: "{spacing.4xl} {spacing.lg}"
---

## Overview

<2-4 sentences describing the design philosophy, mood, and character of the project's visual language.>

## Colors

### Brand & Accent

- **Primary** (`{colors.primary}`) — <usage description>
- **On Primary** (`{colors.on-primary}`) — <usage description>

### Surface

- **Canvas** (`{colors.canvas}`) — <usage description>
- **Canvas Soft** (`{colors.canvas-soft}`) — <usage description>

### Text

- **Ink** (`{colors.ink}`) — <usage description>
- **Body** (`{colors.body}`) — <usage description>
- **Mute** (`{colors.mute}`) — <usage description>

### Semantic

- **Link** (`{colors.link}`) — <usage description>
- **Success** (`{colors.success}`) — <usage description>
- **Error** (`{colors.error}`) — <usage description>
- **Warning** (`{colors.warning}`) — <usage description>

## Typography

### Font Family

<Describe the font stack and any special typographic voice.>

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | <px> | <weight> | <px> | <px> | <use case> |
| `{typography.display-lg}` | <px> | <weight> | <px> | <px> | <use case> |
| `{typography.display-md}` | <px> | <weight> | <px> | <px> | <use case> |
| `{typography.body-lg}` | <px> | <weight> | <px> | <px> | <use case> |
| `{typography.body-md}` | <px> | <weight> | <px> | — | <use case> |
| `{typography.body-sm}` | <px> | <weight> | <px> | <px> | <use case> |
| `{typography.caption}` | <px> | <weight> | <px> | — | <use case> |
| `{typography.code}` | <px> | <weight> | <px> | <px> | <use case> |
| `{typography.button}` | <px> | <weight> | <px> | — | <use case> |

### Principles

- <rule 1>
- <rule 2>

## Layout & Spacing

### Spacing System

- **Base unit**: <N>px. All spacing values are multiples of this unit.
- **Tokens**: `{spacing.xs}` — <px>, `{spacing.sm}` — <px>, `{spacing.md}` — <px>, `{spacing.lg}` — <px>, `{spacing.xl}` — <px>, ...

### Grid & Container

- **Max width**: ~<N>px. Content centres with horizontal gutters.
- **Column patterns**: <describe typical layouts>

### Whitespace Philosophy

<Describe how whitespace is used in the design.>

## Shapes & Elevation

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | <use case> |
| `{rounded.sm}` | <px> | <use case> |
| `{rounded.md}` | <px> | <use case> |
| `{rounded.lg}` | <px> | <use case> |
| `{rounded.pill}` | <px> | <use case> |
| `{rounded.full}` | 9999px | <use case> |

### Shadow & Elevation

| Level | Treatment | Use |
|---|---|---|
| Level 0 — Flat | <shadow value> | <use case> |
| Level 1 — Subtle | <shadow value> | <use case> |
| Level 2 — Elevated | <shadow value> | <use case> |

## Components

### Buttons

- **`button-primary`** — <description>. Background `{colors.primary}`, text `{colors.on-primary}`, shape `{rounded.pill}`, label in `{typography.button}`.
- **`button-secondary`** — <description>. Background `{colors.canvas}`, text `{colors.ink}`, shape `{rounded.pill}`, 1px `{colors.hairline}` border.

### Cards & Containers

- **`card-default`** — <description>. Background `{colors.canvas}`, padding `{spacing.lg}`, shape `{rounded.md}`.

### Inputs & Forms

- **`form-input`** — <description>. Background `{colors.canvas}`, 1px `{colors.hairline}` border, shape `{rounded.sm}`, height <N>px.

### Navigation

- **`nav-bar`** — <description>. Background `{colors.canvas}`, height <N>px.
- **`footer`** — <description>. Background `{colors.canvas}`, padding `{spacing.4xl} {spacing.lg}`.

## Do's and Don'ts

### Do

- <guideline 1>
- <guideline 2>
- <guideline 3>
- <guideline 4>
- <guideline 5>

### Don't

- <anti-pattern 1>
- <anti-pattern 2>
- <anti-pattern 3>
- <anti-pattern 4>
- <anti-pattern 5>
