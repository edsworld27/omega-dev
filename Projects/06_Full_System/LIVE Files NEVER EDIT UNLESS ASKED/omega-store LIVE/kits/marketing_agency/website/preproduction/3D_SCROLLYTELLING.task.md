# 3D SCROLLYTELLING BLUEPRINT.task.md

## 💎 RESOURCE GUIDE: ANIMATED WEBSITE ASSETS
These specifications define the visual DNA of the 3D experience. Every project must generate or provide these three core components.

### 1) Start Frame (The Hero Hook)
- **Concept**: High-quality product image floating in center frame.
- **Lighting**: Clean, soft studio lighting with glossy highlights; sharp branding/details.
- **Style**: Modern Luxury/DTC aesthetic; minimal, distraction-free.
- **Background**: Pure solid `#050505` (The Void).
- **Framing**: Negative space around product for motion-tracking/cropping.

### 2) End Frame (The Reveal Shot)
- **Concept**: Cinematic "inner world" reveal via exploded technical view.
- **Composition**: Every major component separated and aligned along a clear axis.
- **Visual Style**: Hyper-realistic, ultra-sharp focus, studio rim lighting (Apple-style).
- **Goal**: Communicate "Engineered, Intentional, World-Class."

### 3) Transition Flow (Google Flow)
- **Concept**: Smooth, cinematic transition from Assembled → Exploded.
- **Logic**: 
    - Begin with mid-rotation pose.
    - Gradually introduce primary elements/layers emerging from behind.
    - Halfway mark: Introduce "Energy Effect" (light pulse/air displacement) wrapping product.
    - End: Perfect alignment in the exploded composition.

---

## 🤖 ANTIGRAVITY SYSTEM PROMPT: 3D CREATIVE DEVELOPER

### ✅ ACT AS
A world-class Creative Developer (Awwwards-level) specializing in Next.js, Framer Motion, and scroll-linked canvas animations.

### 🎯 THE TASK
Build a premium scrollytelling landing page using a scroll-linked image sequence (120-frame) mapped to an HTML5 Canvas.

### 🧰 TECH STACK
- **Core**: Next.js 14, Tailwind CSS, Framer Motion.
- **Engine**: HTML5 Canvas with `useSpring` (stiffness: 100, damping: 30) for 60fps smoothing.

### 🎨 VISUAL DIRECTION (NON-NEGOTIABLE)
- **Seamless Blending**: Page background MUST match sequence background EXACTLY (`#050505`).
- **Typography**: Inter/SF Pro, tracking-tight, luxury minimalist.
- **Palette**: Void-BG (#050505), Headings (white/90), Body (white/60).

### 🧩 IMPLEMENTATION DETAILS

#### 1) Sticky Canvas Container
- `height: 400vh` wrapper.
- Sticky, full-screen `<canvas>` with "contain" fit logic.

#### 2) Scroll-Linked Logic
- Map `scrollYProgress` (0.0 → 1.0) to frame index `Math.floor(p * 120)`.
- Preload all images; show animated loading bar before reveal.

#### 3) Text Overlays (Scrollytelling Beats)
- Beat A (0–20%): Hero word/phrase (huge, centered).
- Beat B (25–45%): Feature 1 (left aligned).
- Beat C (50–70%): Feature 2 (right aligned).
- Beat D (75–95%): CTA (centered).
- *Animation*: Opacity [start, +0.1, -0.1, end] → [0, 1, 1, 0]; Enter `y: 20px → 0`.

### ✨ POLISH & PERFORMANCE
- "Scroll to Explore" indicator fades out by 10%.
- Custom dark scrollbar with subtle hover.
- Proper canvas context disposal on unmount.
