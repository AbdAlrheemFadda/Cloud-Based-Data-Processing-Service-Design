# WordPress Implementation Guide - Professional Restaurant Landing Page

This guide explains how to recreate the restaurant landing page shown in the assignment image using WordPress.

## Tools Recommended
- **Theme:** Astra (Free, lightweight, and highly customizable).
- **Page Builder:** Elementor (Free version is sufficient for this layout).
- **Images:** High-resolution placeholder images from Unsplash (search for "New York street", "Cherry blossom", "Reflecting pool architecture").

---

## Step 1: Theme and Plugin Installation
1. Go to **Appearance > Themes > Add New** and search for "Astra". Install and Activate it.
2. Go to **Plugins > Add New** and search for "Elementor". Install and Activate it.
3. Create a new page named "Home" and click **Edit with Elementor**.

---

## Step 2: Hero Section (Top)
1. **Container Settings:**
   - Drag a "Container" (Flexbox) to the page.
   - Set "Minimum Height" to `100vh`.
   - Go to **Style > Background**: Upload the NYC street image.
   - Set "Position" to `Center Center`, "Repeat" to `No-repeat`, and "Display Size" to `Cover`.
   - Go to **Background Overlay**: Add a Classic black overlay with `0.5` opacity.
2. **Content:**
   - **Small Heading:** Text "GOOD PLACE. GOOD FOOD.", HTML Tag `H5`, Color `White`, Center Align.
   - **Main Heading:** Text "A Really Good Place To Eat In The City Of New York", HTML Tag `H1`, Size `64px`, Color `White`, Center Align.
   - **Description:** Text "Massa praesent ut suspendisse ac volutpat amet...", HTML Tag `P`, Color `White`, Center Align.
   - **Button:** Text "BOOK A TABLE NOW", Link `#`, Size `Large`.
     - **Style:** Background Color `#50E380`, Text Color `Black`, Border Radius `25px`.

---

## Step 3: Discover Section (Middle)
1. **Container Layout:**
   - Create a new section with two main columns (60% / 40% split).
2. **Left Column:**
   - **Heading:** "Discover The Good Atmosphere Of NYUS.", Size `H2`, Color `Black`.
   - **Description:** "Neque elit, rutrum in laoreet nec...", Size `16px`, Color `Gray`.
   - **Feature (Good Vibes):**
     - Add an "Image" widget (Vertical cherry blossom image).
     - Add a "Heading" below: "Good Vibes", Size `H4`.
     - Add a "Text Editor": "In total 650m² of hand-crafted decor...".
3. **Right Column:**
   - **Feature (Cozy Place):**
     - Add an "Image Box" widget.
     - Upload the horizontal lake/tree image.
     - Title: "Cozy Place", Description: "To make everyone entering...".
   - **Feature (Relax Atmosphere):**
     - Add another "Image Box" widget.
     - Upload the cherry blossom branch image.
     - Title: "Relax Atmosphere", Description: "Take refuge in our exclusive haven...".

---

## Step 4: Signature Menu Section (Bottom)
1. **Container Settings:**
   - Drag a "Container" to the page.
   - Set "Minimum Height" to `60vh`.
   - Go to **Style > Background**: Upload the architecture reflecting pool image.
   - Go to **Background Overlay**: Add a dark overlay with `0.6` opacity.
   - Set content alignment to **Left**.
2. **Content:**
   - **Small Label:** "HOMEMADE", HTML Tag `H6`, Color `White`.
   - **Heading:** "Signature Menu", Size `H2`, Color `White`.
   - **Description:** "Neque elit, rutrum in laoreet nec...", Color `White`.
   - **Button:** "BOOK A TABLE NOW", Background Color `#50E380`, Border Radius `25px`.

---

## Step 5: Required Screenshots for Submission
To fulfill the assignment requirements, take the following screenshots from your WordPress dashboard:
1. **Elementor Editor View:** Showing the Hero Section selected and the "Style" tab visible in the left panel.
2. **Responsive Mode:** Showing how the page looks on a Mobile device.
3. **Background Overlay Settings:** Showing the opacity and color settings for the Hero section.
4. **Final Preview:** A full-page screenshot of the finished landing page.
