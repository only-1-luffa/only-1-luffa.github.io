# Personal Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify a static personal homepage, first technical blog post, and coursework report draft for the Algorithm Foundations assignment.

**Architecture:** The project is a static HTML/CSS site with one homepage and one blog page. A Python acceptance script verifies required content, links, and report files without requiring a web framework or package installation.

**Tech Stack:** HTML5, CSS3, small local Python verification script, GitHub Pages deployment.

---

### Task 1: Acceptance Checks

**Files:**

- Create: `tests/site_checks.py`

- [x] **Step 1: Write the failing test**

Create a script that checks for required public files and links before implementation.

- [x] **Step 2: Run test to verify it fails**

Run: `python tests/site_checks.py`

Expected before implementation: FAIL because `site/index.html` and related files do not exist.

### Task 2: Static Site

**Files:**

- Create: `site/index.html`
- Create: `site/blog/gps-gaussian-plus-camera-views.html`
- Create: `site/styles/main.css`
- Create: `site/AGENTS.md`

- [ ] **Step 1: Implement homepage**

Add homepage sections for identity, public profile, focus areas, learning records, and blog entry.

- [ ] **Step 2: Implement blog page**

Add a learning-note style blog post on GPS-Gaussian+, fixed camera positions, and real-time 3D streaming.

- [ ] **Step 3: Implement shared styling**

Add responsive layout, readable typography, compact cards, and stable button/link dimensions.

- [ ] **Step 4: Re-run checks**

Run: `python tests/site_checks.py`

Expected after Task 2 and Task 3: PASS except any report-specific check until report exists.

### Task 3: Coursework Report Draft

**Files:**

- Create: `report/homework-report.md`

- [ ] **Step 1: Write report draft**

Include homepage introduction, blog introduction, implementation process, AI Agent usage, result display instructions, and deployment link placeholders.

- [ ] **Step 2: Re-run checks**

Run: `python tests/site_checks.py`

Expected: PASS.

### Task 4: Manual Verification

**Files:**

- Read: `site/index.html`
- Read: `site/blog/gps-gaussian-plus-camera-views.html`

- [ ] **Step 1: Start a local static server**

Run from `site`: `python -m http.server 8000`

- [ ] **Step 2: Visit pages**

Open:

- `http://localhost:8000/`
- `http://localhost:8000/blog/gps-gaussian-plus-camera-views.html`

- [ ] **Step 3: Verify links and responsive layout**

Check homepage to blog, blog to homepage, and GitHub profile link.

### Task 5: Deployment Handoff

**Files:**

- Update if needed: `report/homework-report.md`

- [ ] **Step 1: Prepare GitHub Pages instructions**

Recommend deploying to `only-1-luffa.github.io` for the clean URL `https://only-1-luffa.github.io/`.

- [ ] **Step 2: Note remaining user-owned fields**

List student ID, final deployed URL, screenshots, and optional PDF export as remaining steps.

