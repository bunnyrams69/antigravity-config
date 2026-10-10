---
name: screenshot-to-code
description: Convert screenshots, mockups, Figma designs, wireframes, or UI images into clean, responsive, and functional code (HTML/Tailwind, React, Vue, Ionic, Bootstrap). Use whenever the user provides an image or screenshot and asks to code it, recreate a design, build a replica page, or clone a UI.
---

# Screenshot to Code

Convert screenshots, mockups, design images, or wireframes into pixel-accurate, responsive, and accessible code. Based on the proven architecture and prompting methodology of [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code).

---

## 1. Core Principles

1. **Pixel & Text Fidelity**: Replicate the exact layout, margins, padding, colors, and typography from the screenshot. Use the exact text verbatim from the image.
2. **Component & Semantic Structure**: Build clean, semantic HTML with appropriate headings, navbars, buttons, form inputs, grids, and cards.
3. **Responsive by Default**: Mobile-first or desktop layout depending on the input; always ensure flex/grid wrappers break gracefully on mobile viewports.
4. **Standalone Previews**: By default, generate fully self-contained code that can run directly in a browser or HTML preview without complex build steps, using CDNs. If the user is inside an existing React/Vue/Next.js repo, output components matching the repo's structure.

---

## 2. Step-by-Step Procedure

### Step 1: Visual Inspection & Planning
Analyze the input image along these dimensions:
* **Layout Structure**: Header/nav, hero section, grid columns, sidebar, main content, cards, footer.
* **Color Palette**: Background colors, primary accent, secondary buttons, subtle borders, text contrast.
* **Typography**: Font family (match with Google Fonts if custom), font weights, line-heights, letter spacing.
* **Iconography**: Identify icons and map them to Font Awesome, Lucide, or inline SVGs.
* **Interactive Elements**: Hover states, dropdowns, modal dialogs, tabs, inputs.

### Step 2: Choose Target Stack
Consult the user or inspect the workspace for the desired stack:
* **`html_tailwind`** (Default): Standalone HTML with `<script src="https://cdn.tailwindcss.com"></script>`.
* **`react_tailwind`**: React 18 + Babel Standalone + Tailwind CDN (runnable standalone or as a modular `.tsx` component).
* **`vue_tailwind`**: Vue 3 global build + Tailwind CDN.
* **`ionic_tailwind`**: Ionic mobile UI components + Tailwind.
* **`bootstrap`**: Standard Bootstrap 5.3 + icons.
* **`html_css`**: Vanilla HTML5 and pure CSS without utility frameworks.

See [references/stacks.md](references/stacks.md) for the exact CDN tags and boilerplate.

### Step 3: Handle Media & Assets
* **Images**:
  - If the user provided local image assets, link them directly.
  - If images need to be generated or downloaded, use Unsplash (`https://images.unsplash.com/...`) with relevant descriptive keywords.
  - For placeholders, use `https://placehold.co/WIDTHxHEIGHT/BACKGROUND/FOREGROUND?text=Label`.
* **Logos & Custom Shapes**:
  - Replicate brand logos, custom geometric badges, or illustrations using clean inline `<svg>` code.
* **Icons**:
  - Include Font Awesome: `<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">`
  - Or use SVG icons (Lucide/Heroicons inline).

### Step 4: Write Clean Code
* Output the complete, working code.
* If creating a standalone prototype, save it as `index.html` or preview it via an artifact.
* Use meaningful class names and consistent Tailwind utility spacing.

### Step 5: Visual Verification & Targeted Edits
* Compare the generated result against the original screenshot.
* If any element is misaligned, has incorrect padding, or mismatched colors, perform **targeted edits**:
  - Locate the exact outerHTML/element producing the mismatch.
  - Update only that element without rewriting unrelated code.

---

## 3. Local Fullstack App

If you wish to run the full `screenshot-to-code` web application locally (with live side-by-side screenshot upload and streaming code generation):
* Repository location: `e:\common folder\screenshot-to-code`
* See [references/local-app.md](references/local-app.md) for configuration and startup instructions.
