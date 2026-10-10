# Proven Prompt Directives & Policies (from screenshot-to-code)

The following prompting policies and instructions are distilled directly from `abi/screenshot-to-code`'s backend engine:

---

## 1. High-Precision Replication Directives

* **Exact Match**: Make sure the generated page looks exactly like the screenshot.
* **Exact Text**: Use the exact text verbatim from the screenshot (do not invent placeholder text like "Lorem ipsum" if real copy is visible).
* **Asset Handling**:
  - Replicate image containers with appropriate aspect ratios.
  - If assets are visible photos/avatars, use relevant stock photos from Unsplash or clean placeholder SVGs.
  - If icons are visible, find matching icons in Font Awesome or render SVG icons directly.
  - Never embed the raw screenshot image itself as an image tag to cheat the layout. The entire page must be written in code.

## 2. Multi-Screenshot Rules

If multiple screenshots are provided:
* If they represent different pages of a site: create distinct page sections or mock router views.
* If they represent different tabs/states of an app: implement functional tabs/navigation so the user can click through the states.
* If mobile screenshots are provided: focus purely on the application UI, omitting outer phone bezels, notch mockups, or system battery bars unless explicitly asked.

## 3. Targeted Element Edits (Iterative Refinement)

When adjusting a generated page:
* Use the targeted element outerHTML as a locator.
* Match by tag, classes, attributes, and text.
* Modify only the targeted element and its child elements, leaving the surrounding layout untouched.

## 4. Design System Adherence

When given an existing design system (tokens, colors, typography):
* Strict adherence: if design system rules conflict with the screenshot, prioritize the design system tokens for color values and fonts.
* Ensure consistent border-radius, font sizes, and shadow tokens.
